n = int(input())
x = list(input().split())
tot = 0
for s in x:
    if int(s) < 0 :
        tot += 1
print(tot)