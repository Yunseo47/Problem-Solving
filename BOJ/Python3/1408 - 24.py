h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
ds = s2 - s1
dm = m2 - m1
dh = h2 - h1
if ds < 0:
    ds += 60
    dm -= 1
if dm < 0:
    dm += 60
    dh -= 1
if dh < 0:
    dh += 24
dh, dm, ds = map(lambda x: str(x).zfill(2), [dh, dm, ds])
print(dh,dm,ds, sep=':')