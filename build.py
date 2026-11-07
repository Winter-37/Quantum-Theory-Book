#!/usr/bin/env python3
"""Build index.html from tree.txt and the Markdown notes in notes/.

    python3 build.py            build once
    python3 build.py --watch    rebuild whenever a note, tree.txt or the page template changes

Needs one package:  pip install markdown
Viewing the result needs nothing: open index.html in any browser.
"""
import argparse
import html
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTES = ROOT / "notes"
TREE = ROOT / "tree.txt"
PAGE = ROOT / "src" / "page.html"
OUT = ROOT / "index.html"

STATUSES = ("not-started", "in-progress", "complete", "needs-revision")
WORDS_PER_MIN = 260


# ----------------------------------------------------------------------------
# folder tree
# ----------------------------------------------------------------------------
def read_tree():
    """Folder keys in tree order, e.g. '04_X/03_Y/RHF' (parents come before children)."""
    keys, path = [], []
    for n, raw in enumerate(TREE.read_text(encoding="utf-8").splitlines(), 1):
        t = raw.strip()
        if not t or t.startswith("#"):
            continue
        if "\t" in raw:
            sys.exit(f"tree.txt line {n}: use two spaces for indentation, not tabs")
        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2:
            sys.exit(f"tree.txt line {n}: indentation must be a multiple of two spaces")
        depth = indent // 2
        if depth > len(path):
            sys.exit(f"tree.txt line {n}: '{t}' is indented too deeply; a folder can only sit one level below its parent")
        del path[depth:]
        path.append(t)
        key = "/".join(path)
        if key in keys:
            print(f"  warning: tree.txt line {n}: duplicate folder {key}")
            continue
        keys.append(key)
    return keys


def ensure_dirs(keys):
    NOTES.mkdir(exist_ok=True)
    for k in keys:
        (NOTES / k).mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------------------------
# front matter
# ----------------------------------------------------------------------------
def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def _clean(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v


def _split_commas(s):
    out, cur, depth = [], "", 0
    for ch in s:
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
            continue
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        cur += ch
    if cur.strip():
        out.append(cur)
    return [_clean(x) for x in out if x.strip()]


def parse_front(text):
    """Tiny YAML subset: 'key: value', 'key: [a, b]', and 'key:' followed by '- item' lines."""
    text = text.lstrip("﻿")
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    if not m:
        return {}, text
    meta, key = {}, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li and key:
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(_clean(li.group(1)))
            continue
        k, _, v = line.partition(":")
        key = k.strip().lower()
        v = v.strip()
        if v == "":
            meta[key] = []
        elif v.startswith("[") and v.endswith("]"):
            meta[key] = _split_commas(v[1:-1])
        else:
            meta[key] = _clean(v)
    return meta, text[m.end():]


def as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


def as_str(v):
    if isinstance(v, list):
        return v[0] if v else ""
    return v or ""


# ----------------------------------------------------------------------------
# Markdown + math
# ----------------------------------------------------------------------------
FENCE = re.compile(r"(?ms)^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$")
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
DISPLAY_DOLLAR = re.compile(r"(?ms)^(?P<ind>[ \t]*(?:>[ \t]*)*)\$\$(?P<m>.+?)\$\$")
DISPLAY_BRACKET = re.compile(r"(?ms)^(?P<ind>[ \t]*(?:>[ \t]*)*)\\\[(?P<m>.+?)\\\]")
DISPLAY_LOOSE = re.compile(r"(?s)\$\$(.+?)\$\$")
INLINE_PAREN = re.compile(r"(?s)(?<!\\)\\\((.+?)\\\)")
INLINE_DOLLAR = re.compile(r"(?<![\\$])\$(?=[^\s$])((?:\\.|[^$\\\n])+?)(?<=[^\s\\])\$(?![\d$])")
WIKILINK = re.compile(r"\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]")
FILE_EXT = r"pdf|png|jpe?g|svg|gif|webp|txt|csv|py|ipynb|zip|json|xyz|cif|mol|log|out"


class Renderer:
    def __init__(self, resolver):
        import markdown  # imported here so new_note.py can reuse read_tree() without it

        self.md = markdown.Markdown(
            extensions=["tables", "fenced_code", "admonition", "sane_lists", "md_in_html"],
            output_format="html",
        )
        self.resolver = resolver

    def render(self, body, note_dir, links, unresolved):
        stash = {"code": [], "disp": [], "inl": []}

        def put(kind, value, token):
            stash[kind].append(value)
            return f"Z{token}{len(stash[kind]) - 1}Z"

        # 1. code (so nothing inside it is touched)
        body = FENCE.sub(lambda m: put("code", m.group(0), "CODE"), body)
        body = INLINE_CODE.sub(lambda m: put("code", m.group(0), "CODE"), body)

        # 2. math
        def disp_at_line_start(m):
            ind = m.group("ind")
            return f"\n{ind}\n{ind}" + put("disp", m.group("m").strip(), "MATHDISP") + f"\n{ind}\n"

        body = DISPLAY_DOLLAR.sub(disp_at_line_start, body)
        body = DISPLAY_BRACKET.sub(disp_at_line_start, body)
        body = DISPLAY_LOOSE.sub(lambda m: put("disp", m.group(1).strip(), "MATHDISP"), body)
        body = INLINE_PAREN.sub(lambda m: put("inl", m.group(1).strip(), "MATHINL"), body)
        body = INLINE_DOLLAR.sub(lambda m: put("inl", m.group(1), "MATHINL"), body)

        # any '$' left over is a plain dollar sign (prices, shell prompts): escape it so MathJax
        # in the browser does not pair it with another one and typeset the text between them
        body = re.sub(r"(?<!\\)\$", r"\\$", body)

        # 3. [[wiki links]]
        def wiki(m):
            ref, label = m.group(1).strip(), (m.group(2) or "").strip()
            note = self.resolver(ref)
            if note is not None:
                links.add(note["id"])
                return f'<a class="xref" href="#n.{note["id"]}">{html.escape(label or note["title"])}</a>'
            unresolved.add(ref)
            return f'<span class="planned" title="Not written yet">{html.escape(label or ref)}</span>'

        body = WIKILINK.sub(wiki, body)

        # 4. code back, then Markdown
        body = re.sub(r"ZCODE(\d+)Z", lambda m: stash["code"][int(m.group(1))], body)
        self.md.reset()
        out = self.md.convert(body)

        # 5. tidy the HTML
        out = out.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
        out = re.sub(r"<p>\s*(ZMATHDISP\d+Z)\s*</p>", r"\1", out)

        def fix_path(m):
            attr, url = m.group(1), m.group(2)
            if re.match(r"^(?:[a-z][a-z0-9+.-]*:|/|#|notes/)", url, re.I):
                return m.group(0)
            if attr == "href" and not re.search(r"\.(?:%s)(?:[?#].*)?$" % FILE_EXT, url, re.I):
                return m.group(0)
            prefix = f"notes/{note_dir}/" if note_dir else "notes/"
            return f'{attr}="{prefix}{url}"'

        out = re.sub(r'\b(src|href)="([^"]+)"', fix_path, out)

        # 6. math back
        esc = lambda s: html.escape(s, quote=False)
        out = re.sub(r"ZMATHDISP(\d+)Z", lambda m: '<div class="eq">$$' + esc(stash["disp"][int(m.group(1))]) + "$$</div>", out)
        out = re.sub(r"ZMATHINL(\d+)Z", lambda m: "$" + esc(stash["inl"][int(m.group(1))]) + "$", out)
        return out


def plain_words(htm):
    return len(re.sub(r"<[^>]+>", " ", htm).split())


# ----------------------------------------------------------------------------
# build
# ----------------------------------------------------------------------------
def build():
    t0 = time.time()
    warnings = []
    keys = read_tree()
    ensure_dirs(keys)
    known = set(keys)
    extra_keys = []

    def add_folder(key, why):
        parts = key.split("/")
        for i in range(1, len(parts) + 1):
            k = "/".join(parts[:i])
            if k not in known:
                known.add(k)
                extra_keys.append(k)
                warnings.append(f"folder '{k}' is not in tree.txt ({why}); added at the end of the tree")

    # ---- pass 1: read every note
    records, intros_raw = [], {}
    used_ids = {}
    for p in sorted(NOTES.rglob("*.md")):
        rel = p.relative_to(NOTES)
        if any(part.startswith((".", "_")) for part in rel.parts):
            continue
        key = rel.parent.as_posix()
        key = "" if key == "." else key
        meta, body = parse_front(p.read_text(encoding="utf-8"))
        if key and key not in known:
            add_folder(key, f"notes/{rel.as_posix()}")
        if p.name.lower() == "index.md":
            intros_raw[key] = (body, meta)
            continue
        title = as_str(meta.get("title"))
        m = re.match(r"\s*#[ \t]+(.+?)[ \t]*\r?\n", body)
        if m:
            if not title:
                title = m.group(1).strip()
            body = body[m.end():]
        if not title:
            title = p.stem.replace("_", " ").replace("-", " ")
        nid = slug(as_str(meta.get("id"))) or slug(re.sub(r"^\d+[_-]", "", p.stem)) or slug(title)
        base, n = nid, 2
        while nid in used_ids:
            nid = f"{base}-{n}"
            n += 1
        if nid != base:
            warnings.append(f"duplicate note id '{base}' ({rel.as_posix()}); using '{nid}'")
        used_ids[nid] = rel.as_posix()
        status = slug(as_str(meta.get("status")))
        if status and status not in STATUSES:
            warnings.append(f"{rel.as_posix()}: unknown status '{status}' (use: {', '.join(STATUSES)})")
        order = as_str(meta.get("order"))
        try:
            order = float(order) if order != "" else None
        except ValueError:
            order = None
        records.append({
            "path": rel, "key": key, "meta": meta, "body": body, "id": nid, "title": title,
            "stem": p.stem, "status": status, "order": order,
        })

    # ---- resolver for ids, titles and file names
    lookup = {}
    for r in records:
        for k in (r["id"], slug(r["title"]), slug(r["stem"])):
            lookup.setdefault(k, r)

    def resolver(ref):
        return lookup.get(slug(ref))

    renderer = Renderer(resolver)

    # ---- pass 2: render
    notes_out = []
    unresolved_all = {}
    for r in records:
        meta = r["meta"]
        links, unresolved = set(), set()
        htm = renderer.render(r["body"], r["key"], links, unresolved)

        def refs(field_names):
            out = []
            for f in field_names:
                for ref in as_list(meta.get(f)):
                    note = resolver(ref)
                    if note is None:
                        unresolved.add(ref)
                        out.append(ref)
                    elif note["id"] != r["id"] and note["id"] not in out:
                        out.append(note["id"])
            return out

        prereq = refs(["prerequisites", "prerequisite", "prereq"])
        related = refs(["related"])
        if as_list(meta.get("also")):
            warnings.append(f"{r['path'].as_posix()}: 'also:' is no longer supported (each note has one home); ignored")
        cite = {k: as_str(meta.get(k)) for k in ("authors", "journal", "year", "doi") if as_str(meta.get(k))}
        for ref in sorted(unresolved):
            unresolved_all.setdefault(ref, []).append(r["id"])
        notes_out.append({
            "id": r["id"], "title": r["title"], "summary": as_str(meta.get("summary")),
            "date": as_str(meta.get("date")), "status": r["status"],
            "level": slug(as_str(meta.get("level"))), "kind": slug(as_str(meta.get("kind"))),
            "tags": [t for t in as_list(meta.get("tags")) if t],
            "prereq": prereq, "related": related, "links": sorted(links - {r["id"]}),
            "home": r["key"], "order": r["order"], "cite": cite,
            "mins": max(1, round(plain_words(htm) / WORDS_PER_MIN)), "html": htm,
        })

    intros = {}
    for key, (body, _meta) in intros_raw.items():
        intros[key] = renderer.render(body, key, set(), set())

    for ref, who in sorted(unresolved_all.items()):
        warnings.append(f"not written yet: '{ref}' (linked from {', '.join(sorted(set(who)))})")

    data = {"folders": keys + extra_keys, "notes": notes_out, "intros": intros}
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    page = PAGE.read_text(encoding="utf-8")
    if "__SITE_DATA__" not in page:
        sys.exit("src/page.html has no __SITE_DATA__ placeholder")
    OUT.write_text(page.replace("__SITE_DATA__", blob), encoding="utf-8")

    n_unres = len(unresolved_all)
    shown = [w for w in warnings if not w.startswith("not written yet")]
    print(f"Built index.html: {len(notes_out)} notes, {len(keys) + len(extra_keys)} folders "
          f"({(time.time() - t0) * 1000:.0f} ms)")
    for w in shown:
        print("  warning:", w)
    if n_unres:
        planned = [w for w in warnings if w.startswith("not written yet")]
        print(f"  {n_unres} linked note(s) not written yet (shown greyed out as 'planned'):")
        for w in planned[:15]:
            print("   -", w[len("not written yet: "):])
        if len(planned) > 15:
            print(f"   ... and {len(planned) - 15} more")


def fingerprint():
    files = [TREE, PAGE] + [p for p in NOTES.rglob("*") if p.is_file()]
    return sorted((str(p), p.stat().st_mtime_ns) for p in files if p.exists())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--watch", action="store_true", help="rebuild on every change (Ctrl+C to stop)")
    args = ap.parse_args()
    try:
        import markdown  # noqa: F401
    except ImportError:
        sys.exit("The 'markdown' package is missing. Install it with:  pip install markdown")
    build()
    if args.watch:
        print("Watching for changes. Press Ctrl+C to stop.")
        last = fingerprint()
        try:
            while True:
                time.sleep(1)
                cur = fingerprint()
                if cur != last:
                    last = cur
                    try:
                        build()
                    except SystemExit as e:
                        print("  error:", e)
        except KeyboardInterrupt:
            print()


if __name__ == "__main__":
    main()
