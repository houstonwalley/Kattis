n = int(input())
result = ''
for i in range(n):
    x = int(input())
    tot = []
    for j in range(x):
        s = str(input())
        if s not in tot:
            tot.append(s)
    result += str(len(tot)) + '\n'
print(result)