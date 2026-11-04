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
python3 new_note.py RHF "Restricted Hartree-Fock"   # creates the file from the template
# edit notes/.../restricted-hartree-fock.md
python3 build.py                                     # rebuild index.html
python3 build.py --watch                             # or: rebuild automatically on every save
```

Then refresh the browser tab. `new_note.py` takes a folder path from `tree.txt`, or just its last
part when that is unique (`RHF`, `06_Reduced_Density_Matrices`). If the name appears in two places
it lists them and asks for the full path. Any folder page in the site shows the exact command to
copy.

You can also create the file by hand: save any `.md` file inside the right folder under `notes/`.
The folder it sits in is the folder it is filed in.

## The folder tree

`tree.txt` holds one folder per line, children indented by two spaces. Edit it to add, rename or
reorder folders, then run `build.py`; it creates the matching folders under `notes/`.
Leading numbers (`04_`) become the folder numbers in the site; unnumbered names sort where you put them.

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
| `also` | Extra folders that should list this note (see below). |
| `order` | Optional number; lower comes first inside a folder. Default: alphabetical by title. |
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

## Notes that belong in two folders

Each note has **one home**: the folder its file sits in. Add `also: [folder/path]` to list it in
other folders as well. There it appears marked **Shortcut**, with its home path, and clicking it
opens the one real note. Nothing is duplicated, so there is only one page to keep correct.

Rules of thumb:

1. Use a shortcut only when the note really belongs to both areas. If you only want a reader of
   folder B to find it, use `related` or `[[a link]]` instead.
2. Choose the home by the most specific folder that fits (a Hartree-Fock derivation lives in
   Hartree-Fock, with a shortcut from Quantum Chemistry, not the other way round).
3. When the same subject appears in several top-level sections of the tree (VQE, embedding,
   potential energy surfaces), split by role rather than copying: theory in one home, software
   details in the software folder, and link them to each other.

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
