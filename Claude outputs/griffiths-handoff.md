# Handoff: fill the Quantum Mechanics section from Griffiths

Paste or attach this file at the start of a new chat. It carries over everything from the previous chat that the new one needs.

## The task

Write notes from **Griffiths, *Introduction to Quantum Mechanics*** for the empty `02_Quantum_Mechanics` section of my offline knowledge-base site. Verify the numbers by computation as you go. Planned after Griffiths, in later chats: Sakurai; Yamaguchi–Osamura–Goddard–Schaefer, *A New Dimension to Quantum Chemistry*; Shavitt–Bartlett; Levine; McWeeny.

**Before writing anything:**

1. Read `CLAUDE.md` in the site root. It is the authoritative style and format guide.
2. Check which edition the PDF is (2nd or 3rd; the chapter numbers differ).
3. Propose a note plan (ids, titles, target folders) and wait for my OK.

## Where things are (on my computer, through the desktop link)

- **Site root:** `/home/ankita/Desktop/Adarsh_files/Scientific_Knowledge`
  - `notes/<folders>/<id>.md`: one note per file. The filename must equal the `id`.
  - `tree.txt`: the folder tree. Ask before adding, renaming or moving folders or ids.
  - `build.py`: generates `index.html`. Never edit `index.html` by hand.
  - `new_note.py`: creates a note from `templates/note.md`.
  - `src/`, `templates/`, `vendor/`: page template, note template, offline MathJax.
  - `CLAUDE.md`, `README.md`.
- **The book:** `books/Griffiths - Introduction to quantum mechanics.pdf` (about 14 MB). The `books/` folder is git-ignored and never published.
- **Hosting:** the folder is a git repo, published with GitHub Pages at https://winter-37.github.io/Quantum-Theory-Book/ (repo `Winter-37/Quantum-Theory-Book`, branch `main`, root). **I push it myself.** After you commit files to my computer, remind me to run:

  ```
  python3 build.py
  git add -A
  git commit -m "..."
  git push
  ```

## Working method that worked well

1. **Set up a workspace copy.** Stage `build.py`, `tree.txt`, `new_note.py`, `CLAUDE.md`, `src/`, `templates/`, `vendor/` and all of `notes/` into the workspace. Build there with `python3 build.py`, and check that it reports no warnings, duplicate ids or broken `[[links]]`.
2. **Get the book text.** Extract it with `pdftotext -layout`; render a page to an image when equations or figures are unclear.
3. **Verify every number by computation** (numpy/scipy/sympy), e.g.:
   - square-well and harmonic-oscillator spectra by finite differences;
   - hydrogen radial functions and expectation values;
   - Clebsch–Gordan coefficients;
   - tunnelling transmission;
   - variational bounds;
   - WKB energies.

   Keep the scripts in a `griffiths/` folder in the workspace and name them in each note's Source section.
4. **Render-check.** Render each new note in headless Chromium (Playwright is installed) and check that the math displays and the tables render. Fix anything broken.
5. **Commit back to my computer.**
   1. Copy the changed notes plus the new `index.html` to `/mnt/user-data/outputs/<batch>/`.
   2. Call `device_list_dir` on the site root to get the `index.html` mtime.
   3. Call `device_commit_files`, passing `expectedMtimeMs` for `index.html`.
   4. If the commit is rejected because the mtime is stale, re-list and retry with the new mtime.
6. **Deleting files.** You cannot delete files on my computer. Tell me which files to remove.

## Note format (summary; `CLAUDE.md` wins on any conflict)

**Front matter fields:**

| Field | Value |
|---|---|
| `id` | kebab-case, equal to the filename |
| `title` | |
| `summary` | |
| `status` | `in-progress` |
| `kind` | one of `theory`, `derivation`, `algorithm`, `implementation`, `comparison`, `paper`, `reference` |
| `level` | |
| `tags` | |
| `prerequisites` | |
| `related` | |
| `also` | |
| `date` | today for new notes; edited notes keep their original date |

**Body:**

- Starts at a `##` heading.
- Display math goes in `$$ … $$` blocks. No physics-package macros (`\ket`, `\bra`, `\expval` and so on); write `\langle … \rangle` and similar.
- Tables use a plain `|`, never `\|`.
- Worked examples are admonitions, `!!! example "Title"`, with the body indented by 4 spaces.
- Cross-link existing notes with `[[note-id]]`.
- End every note with a `## Source` section in the form: "Griffiths, *Introduction to Quantum Mechanics* (Nth ed., publisher, year), Sec. …, pp. …, Eqs. …". Then name the scripts used for recomputation.

**Content rules:**

- Write in my own words. Don't copy text.
- Never fabricate citations.
- Mark anything quoted or unverified as such.
- Don't mention DMET or embedding anywhere in the notes.
- My level: strong quantum-chemistry background. I prefer rigorous derivations with explicit equations and worked numerical examples.

## The QM section and how Griffiths might map onto it

`tree.txt` subfolders of `02_Quantum_Mechanics`, with a suggested mapping for the 3rd edition (adjust for the 2nd):

| Folder | Griffiths material |
|---|---|
| `01_Quantum_Mechanical_Foundations` | Ch. 1: wave function, Born rule, normalization, momentum, uncertainty |
| `02_Schrodinger_Equation` | Ch. 2: stationary states, infinite well, harmonic oscillator (ladder and analytic), free particle, delta and finite wells, scattering states |
| `03_Operators_and_Observables` | Ch. 3: Hilbert space, Hermitian operators, spectra, generalized statistics, generalized uncertainty, Dirac notation |
| `04_Angular_Momentum_and_Spin` | Ch. 4: 3D SE, hydrogen atom, orbital angular momentum, spin, addition of angular momenta |
| `08_Identical_Particles` | Ch. 5: bosons and fermions, exchange forces, atoms, solids |
| `09_Symmetry_and_Group_Theory` | Ch. 6 (3rd ed.): symmetries and conservation laws, parity, rotations, degeneracy |
| `06_Perturbation_Theory` | Ch. 7: time-independent PT, fine structure, Zeeman, hyperfine |
| `05_Approximation_Methods` | Ch. 8–9: variational principle and helium, WKB |
| `10_Quantum_Dynamics` | Ch. 10–11: time-dependent PT, Fermi's golden rule, emission and absorption, adiabatic approximation, Berry phase |
| `07_Many_Particle_Quantum_Mechanics` | likely sparse from Griffiths; leave for Sakurai or McWeeny |
| scattering (Ch. 10 in the 3rd ed.) | there is no scattering folder yet; ask me before adding one to `tree.txt` |

**Existing notes that overlap.** Link to these rather than duplicate them. Where Griffiths adds material, propose extending the existing note or writing a clearly different companion note.

- Already in `02_Quantum_Mechanics`:
  - `rayleigh-schrodinger-perturbation-theory` (in `06_Perturbation_Theory`)
  - `greens-functions-single-particle` (in `05_Approximation_Methods`)
- In `04_Electronic_Structure_Theory/00_Foundations…` and `01_Mathematical…`:
  - `dirac-notation`
  - `orthonormal-functions-and-operators`
  - `change-of-basis`
  - `matrix-eigenvalue-problem`
  - `variational-principle`, `variation-method`, `linear-variation-method`
  - `upper-bounds-and-interlacing`
  - `hellmann-feynman-and-virial-theorems`
  - `spin-operators`
  - `spin-orbitals-and-antisymmetry`
  - `slater-determinants`
  - `atomic-units`
  - `born-oppenheimer-approximation`
  - `molecular-hamiltonian`
  - `exact-wave-function-properties-and-symmetry`
  - `one-particle-hamiltonian-models`
  - `baker-campbell-hausdorff`

**Reading guide.** `09_Reference_Material/reading-order-electronic-structure.md` is a staged reading guide. When the Griffiths notes are done, propose adding them to its Stage 2 (quantum-mechanical foundations).

## Reply format I like

At the end of each batch, reply with:

1. where the notes went;
2. what was checked numerically;
3. corrections to the book and caveats;
4. anything unverified;
5. planned `[[links]]` still unwritten;
6. one next step.

Keep it short.
