n = int(input())
result = ""
for i in range(n):
    x = int(input())
    y = 1
    x = x // 10
    while not x == 0:
        y += 1
        x = x // 10
    result += str(y) + "\n"
print(result)