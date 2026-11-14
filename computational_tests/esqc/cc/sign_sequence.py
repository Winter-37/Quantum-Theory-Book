"""Kucharski-Bartlett sign sequence: distinct connections of V_N(-2 part: 2 particle + 2 hole lines)
to T1, T1, T2 with at least one line from each T (T1's interchangeable)."""
import itertools
T1 = [(p, h) for p in (0, 1) for h in (0, 1) if p + h >= 1]
T2 = [(p, h) for p in (0, 1, 2) for h in (0, 1, 2) if p + h >= 1]
s = {(tuple(sorted([a, b])), c) for a in T1 for b in T1 for c in T2
     if a[0]+b[0]+c[0] == 2 and a[1]+b[1]+c[1] == 2}
print(len(s)); [print(x) for x in sorted(s)]
