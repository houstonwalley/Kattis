cost = float(input())
x = int(input())
tot = 0
for i in range(x):
    yeet = list(input().split())
    w = float(yeet[0])
    l = float(yeet[1])
    tot += w * l * cost

print(tot)