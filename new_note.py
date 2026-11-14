#!/usr/bin/env python3
"""Create a new note from a template.

    python3 new_note.py <folder> "<title>" [--kind paper] [--id my-id]

<folder> is a folder path from tree.txt, or just its last part when that is unique
(for example RHF or 06_Reduced_Density_Matrices). Then edit the new file and run build.py.
"""
import argparse
import datetime
import sys
from pathlib import Path

from build import NOTES, ROOT, read_tree, slug


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    ap.add_argument("title")
    ap.add_argument("--kind", default="note", help="template to use: note (default) or paper")
    ap.add_argument("--id", dest="nid", default="", help="stable id used in links (default: from the title)")
    args = ap.parse_args()

    keys = read_tree()
    want = args.folder.strip().strip("/")
    hits = [k for k in keys if k == want] or [k for k in keys if k.endswith("/" + want) or k == want]
    if not hits:
        sys.exit(f"No folder matches '{want}'. Folders are listed in tree.txt.")
    if len(hits) > 1:
        print(f"'{want}' matches more than one folder. Use the full path:")
        for k in hits:
            print("  ", k)
        sys.exit(1)
    key = hits[0]

    tpl = ROOT / "templates" / f"{'paper' if args.kind == 'paper' else 'note'}.md"
    if not tpl.exists():
        sys.exit(f"Template not found: {tpl}")
    nid = slug(args.nid) or slug(args.title)
    target = NOTES / key / f"{nid}.md"
    if target.exists():
        sys.exit(f"Already exists: {target.relative_to(ROOT)}")
    target.parent.mkdir(parents=True, exist_ok=True)
    text = (tpl.read_text(encoding="utf-8")
            .replace("{{id}}", nid)
            .replace("{{title}}", args.title)
            .replace("{{date}}", datetime.date.today().isoformat()))
    target.write_text(text, encoding="utf-8")
    print(f"Created {target.relative_to(ROOT)}")
    print("Edit it, then run:  python3 build.py")


if __name__ == "__main__":
    main()
