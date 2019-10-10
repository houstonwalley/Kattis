l = int(input())
d = int(input())
x = str(input())
n = d
m = l

dig_tot = int(x)

for i in range(l - 1, d):
    yeet = str(i)
    min_tot = 0
    for y in yeet:
        min_tot += int(y)
    if min_tot == dig_tot:
        n = i
        break

for i in range(d + 1, l, -1):
    yeet = str(i)
    max_tot = 0
    for y in yeet:
        max_tot += int(y)
    if max_tot == dig_tot:
        m = i
        break

print(n)
print(m)