n = list(input().split())
p = [1, 1, 2, 2, 2, 8]
result = ''
for i in range(len(n)):
    result += str(p[i] - int(n[i])) + ' '
print(result)