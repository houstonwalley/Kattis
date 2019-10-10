cards = str(input())
t = 0
c = 0
g = 0
count = 0
for s in cards:
    if s == 'T':
        t += 1
    if s == 'C':
        c += 1
    if s == 'G':
        g += 1


tot = (t ** 2) + (c ** 2) + (g ** 2) + (min(t, c, g) * 7)
print(tot)