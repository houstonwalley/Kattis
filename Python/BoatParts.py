t = list(input().split())
p = int(t[0])
n = int(t[1])
yeet = []
count = 0
for i in range(n):
    part = str(input())
    if part not in yeet:
        yeet.append(part)
        count += 1
        if count == p:
            break
if count == p:
    print('\n' + str(i + 1))
else:
    print('paradox avoided')