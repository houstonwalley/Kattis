n = int(input())
h = 2
for i in range(n):
    h += (h - 1)
print(pow(h, 2))