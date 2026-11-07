# Scientific Knowledge

A personal reference site. You write notes in Markdown; `build.py` turns them into one
`index.html` that opens by double-click in any browser, with no internet and no server.

```
Scientific_Knowledge/
├── index.html        the site (generated). Open this.
├── vendor/           equation renderer and fonts, so everything works offline
├── notes/            your notes. Folders mirror tree.txt; one .md file per note
├── templates/        note.md and paper.md
├── tree.txt          the folder structure and its order
├── src/page.html     the site's design (HTML, CSS, JavaScript)
├── build.py          notes + tree  ->  index.html
└── new_note.py       create a note from a template
```

## One-time setup

```bash
pip install markdown
```

That is only needed to build. Opening `index.html` needs nothing.

## Everyday use

```bash
python3 new_note.py 03_Hartree_Fock_Theory "Restricted Hartree-Fock"   # creates the file from the template
# edit notes/.../restricted-hartree-fock.md
python3 build.py                                     # rebuild index.html
python3 build.py --watch                             # or: rebuild automatically on every save
```

Then refresh the browser tab. `new_note.py` takes a folder path from `tree.txt`, or just its last
part when that is unique (`03_Hartree_Fock_Theory`, `06_Reduced_Density_Matrices`). If the name appears in two places
it lists them and asks for the full path. Any folder page in the site shows the exact command to
copy.

You can also create the file by hand: save any `.md` file inside the right folder under `notes/`.
The folder it sits in is the folder it is filed in.

## The book structure

The notebook is arranged like a book with two folder levels:

- **Parts:** the top-level folders, `04_Electronic_Structure_Theory` for example.
- **Chapters:** the folders inside a part, `04_Electronic_Structure_Theory/03_Hartree_Fock_Theory` for example.
- **Sections:** the notes inside a chapter.

**Numbering.** The site numbers everything from the folder prefixes and the `order` field: Part 4, Chapter 4.3, Section 4.3.5. Every section has **Previous / Next** buttons that walk through the whole book in that order, crossing chapter boundaries. The sidebar is a table of contents, and expanding a chapter lists its sections.

**Chapter introductions.** Each chapter has an `index.md` introduction: what the chapter covers, the path through its sections, what it needs and what it leads to, plus the planned sections still to be written. Keep it up to date when you add a section. Empty chapters are kept and shown as planned.

**`tree.txt`** holds one folder per line, children indented by two spaces. Edit it to add, rename or
reorder parts and chapters, then run `build.py`; it creates the matching folders under `notes/`.
Leading numbers (`04_`) become the numbers in the site; unnumbered names sort where you put them.

If you rename or move a folder that already contains notes, rename the same directory under
`notes/` too (`git mv` keeps history). Notes in a directory that is not in `tree.txt` still appear;
the folder is added at the end of the tree and `build.py` warns you.

A file called `index.md` inside a folder is that folder's introduction. It is shown at the top of
the folder page and is not listed as a note.

## Writing a note

Start from `templates/note.md` (or `paper.md` for a literature summary). The block between the
two `---` lines is metadata:

| Field | Meaning |
|---|---|
| `id` | Stable name used in links and in the address (`index.html#n.<id>`). Do not change it once other notes link to it. Default: the file name. |
| `title` | Page title. Default: the first `# Heading`, else the file name. |
| `summary` | One or two sentences for folder lists and search. |
| `status` | `not-started`, `in-progress`, `complete` or `needs-revision`. |
| `kind` | `theory`, `derivation`, `algorithm`, `implementation`, `comparison`, `paper`, `reference`. Each kind gets an index on the home page. |
| `level` | `introductory`, `intermediate` or `advanced`. |
| `tags` | `[a, b]`. Searched, shown on the note. |
| `prerequisites` | Notes to understand first, by id or title. Shown at the top of the note. |
| `related` | Connected notes that are not prerequisites. |
| `order` | Position of the section inside its chapter (lower first). Use steps of 10 so a new section can be slotted in between. The template's 999 puts a new section at the end. Default: alphabetical by title. |
| `date` | `YYYY-MM-DD`, optional. |
| `authors`, `journal`, `year`, `doi` | For papers. |

Everything is optional except that a note needs some text. Any field can be left out.

### Links between notes

- `prerequisites` and `related` in the metadata. The page also builds **Required by** (notes that
  list this one as a prerequisite) and **Mentioned in** (notes that relate to or link to it)
  automatically.
- In the text, `[[note id or title]]` or `[[note id|label to show]]`.
- A link to a note you have not written yet is fine. It shows greyed out as "planned", becomes a
  link once the note exists, and `build.py` lists what is still unwritten.

### Equations

- Inline: `$E=mc^2$`. Display: put `$$ ... $$` on its own lines. `\( ... \)` and `\[ ... \]` also work.
- Write LaTeX normally. Underscores, stars and `<` are safe inside math. Math inside code spans or
  code blocks is left alone.
- Inside a table cell, write `|` normally in math (`$\langle a|b\rangle$`). Do not write `\|`, which
  means the double bar $\|$.
- A single `$` that is not math (a price, for example) is shown as a plain dollar sign.

### Other Markdown

Tables, fenced code blocks (` ```python `), lists, images and links work. For boxed blocks use
admonitions, with a blank line before and everything indented four spaces:

```markdown
!!! example "Worked example"
    Text here, and equations if you like.
```

Types: `example`, `note`, `warning`.
Images and file links are relative to the note: `![diagram](rhf.png)` finds `rhf.png` next to the
note. Keep `notes/` next to `index.html` when you move or publish the site.

## One note, one place

Each note lives in exactly one chapter: the folder its file sits in. There are no shortcuts or
duplicate listings. To connect a note to another chapter, use `prerequisites`, `related` or
`[[a link]]`. `build.py` warns if an old `also:` field is still present and ignores it.

When the same subject turns up in several parts (VQE, embedding, potential energy surfaces), split it
by role rather than copying: theory in one chapter, software details in the software chapter, and
link the two.

## Look and feel

Fonts and colours are the variables at the top of `src/page.html` (`--display`, `--serif`,
`--mono`, and the colour tokens). To use another font offline, put its `.woff2` file in
`vendor/fonts/` and add an `@font-face` line next to the existing ones. Run `build.py` afterwards.

## Backup and publishing

Keep the folder in Git. `index.html` is generated, but keeping it in the repository means the site
works straight after a clone. Git does not track empty folders; `build.py` recreates them from
`tree.txt`.

To publish later, upload `index.html`, `vendor/` and `notes/` to GitHub Pages, Netlify or
Cloudflare Pages.
