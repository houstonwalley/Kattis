n = list(input().split())
l = int(n[0])
x = int(n[1])
tot = 0
groups = 0
for i in range(x):
    line = list(input().split())
    num = int(line[1])
    if line[0] == 'enter':
        if tot + num <= l:
            tot += num
        else:
            groups +=1
    else:
        tot -= num

print(groups)