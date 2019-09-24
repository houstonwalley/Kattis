n = int(input())
num = []
tot = 0
for i in range(n):
    num.append(str(input()))
for s in num:
    x = int(s[:-1])
    y = int(s[-1:])
    tot += pow(x, y)
print(tot)