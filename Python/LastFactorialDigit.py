n = int(input())
result = ""
for i in range(n):
    j = int(input())
    tot = 1
    while j > 0:
        tot = tot * j
        j = j - 1
    if result == "":
        yeet = str(tot)
        result += yeet[-1:]
    else:
        yeet = str(tot)
        result += "\n" + yeet[-1:]
print(result)