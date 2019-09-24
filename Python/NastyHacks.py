n = int(input())
result = ""
for i in range(n):
    line = list(input().split())
    yeet = int(line[1]) - int(line[2])
    if result == "":
        if yeet > int(line[0]):
            result += "advertise"
        elif yeet == int(line[0]):
            result += "does not matter"
        else:
            result += "do not advertise"
    else:
        if yeet > int(line[0]):
            result += "\nadvertise"
        elif yeet == int(line[0]):
            result += "\ndoes not matter"
        else:
            result += "\ndo not advertise"
print(result)