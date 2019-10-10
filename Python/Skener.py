n = list(input().split())
r = int(n[0])
c = int(n[1])
row = int(n[2])
col = int(n[3])
result = ''
lines = []
for i in range(r):
    lines.append(input())
for s in lines:
    line = ''
    for i in range(c):
        for j in range(col):
            line += s[i]
    for i in range(row):
        result += line + '\n'
print(result)
