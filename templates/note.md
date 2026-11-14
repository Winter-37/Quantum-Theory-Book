---
# HOW TO USE THIS TEMPLATE
# Run:  python3 new_note.py <folder> "Title"      (it copies this file into notes/<folder>/)
# Everything between the two --- lines is metadata. Lines starting with # are comments.
# Delete any section below you do not need. A note on SVD does not need "Physical interpretation".

# Stable name used in links. Do not change it after other notes link to this one.
id: {{id}}
title: {{title}}
# One or two sentences, shown in folder lists and search results.
summary: What this note establishes, in one or two sentences.
# not-started | in-progress | complete | needs-revision
status: in-progress
# theory | derivation | algorithm | implementation | comparison | reference
kind: theory
# introductory | intermediate | advanced
level: intermediate
tags: []
# What to understand first. Use note ids or titles. Notes you have not written yet are fine:
# they show greyed out as "planned" and become links once the note exists.
prerequisites: []
# Connected topics that are not prerequisites.
related: []
# Position inside the chapter (sections are numbered in this order). Use steps of 10 so you can insert later.
order: 999
date: {{date}}
---

## Overview

What is this, what problem does it address, and why does it matter? Two or three sentences.

## Notation and definitions

Define every symbol before using it, and say which convention you follow.
Link other notes by id or title with double square brackets, for example `[[Second Quantization Notation]]`.

## Key results

The equations you will want to look up later, stated without proof:

$$
\hat H \Psi = E \Psi
$$

## Derivation

State the assumptions first. Then give each step with the reason for it.
Inline math uses single dollar signs, like $\gamma_{pq}=\langle\Psi|a_p^\dagger a_q|\Psi\rangle$.
Display equations go on their own lines between double dollar signs.

## Physical interpretation

What do the equations mean physically? Which limits can be checked?

## Worked example

!!! example "Worked example"
    Use a system small enough to do by hand, with explicit numbers, and check the
    result against a known value. Indent everything in this block by four spaces.

    | Quantity | Value |
    |---|---:|
    | E (Eh) | -1.1167 |

## Computational formulation

How the theory becomes a procedure. Give the steps in order and the cost scaling, for example $O(N^4)$.

1. Step one.
2. Step two.

## Implementation

Software, the function or class that does it, input parameters, and output quantities.

```python
from pyscf import gto, scf

mol = gto.M(atom="H 0 0 0; H 0 0 0.74", basis="sto-3g")
mf = scf.RHF(mol).run()
print(mf.e_tot)
```

## Limitations

Where does it fail? Which approximations limit accuracy? What does it cost?

## Open questions

Things to check, unresolved points, possible research directions.

## References

1. Book, chapter or section.
2. Paper (authors, journal, year, DOI).
3. Documentation.
