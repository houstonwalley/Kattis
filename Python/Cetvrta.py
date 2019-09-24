n1 = list(input().split())
n2 = list(input().split())
n3 = list(input().split())
x = 0
y = 0
if n1[0] == n2[0]:
    x = n3[0]
elif n1[0] == n3[0]:
    x = n2[0]
else:
    x = n1[0]
if n1[1] == n2[1]:
    y = n3[1]
elif n1[1] == n3[1]:
    y = n2[1]
else:
    y = n1[1]
print(str(x) + " " + str(y))