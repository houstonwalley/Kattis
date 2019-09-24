n = list(input().split())
i = n[0]
j = n[1]
x = int(i[2] + i[1] + i[0])
y = int(j[2] + j[1] + j[0])
if x > y:
    print(i[2] + i[1] + i[0])
else:
    print(j[2] + j[1] + j[0])