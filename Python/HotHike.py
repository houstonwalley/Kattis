n = int(input())
x = list(input().split())
days = []
for i in range(n - 2):
    if int(x[i]) > int(x[i + 2]):
        days.append(x[i])
    else:
        days.append(x[i + 2])
small = 1000
point = 0
for t in range(n - 2):
    if int(days[t]) < int(small):
        small = days[t]
        point = t + 1
print(str(point) + ' ' + str(small))