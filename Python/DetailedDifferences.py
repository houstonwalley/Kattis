n = int(input())
result = ''
for i in range(n):
    x = input()
    y = input()
    line = ''
    for j in range(len(x)):
        if x[j] == y[j]:
            line += '.'
        else:
            line += '*'
    result += x + '\n'
    result += y + '\n'
    result += line + '\n\n'
print(result)