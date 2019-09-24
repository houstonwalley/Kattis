n = int(input())
result = ""
for i in range(n):
    x = int(input())
    if result == "":
        if x % 2 == 0:
            result += str(x) + " is even"
        else:
            result += str(x) + " is odd"
    else:
        if x % 2 == 0:
            result += "\n" + str(x) + " is even"
        else:
            result += " \n" + str(x) + " is odd"
print(result)