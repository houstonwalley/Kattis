n = str(input())
x = len(n)
for i in range(len(n) - 1):
    for j in range(i + 1, len(n)):
        m = n[i:j]
        t = n.replace(m, 'm')
        v = len(t) + len(m)
        x = min(x, v)
print(x)
