n = int(input())
result = ''
for i in range(n):
    x = list(input().split())
    b = int(x[0])
    p = float(x[1])
    result += str(format((60 * (b - 1) / p), '0.4f')) + ' ' + str(format((60 * b / p), '0.4f')) + ' ' + str(format((60 * (b + 1) / p), '0.4f')) + '\n'
print(result)