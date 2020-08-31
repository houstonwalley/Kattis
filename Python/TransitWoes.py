line = input().split()
s = int(line[0])
t = int(line[1])
n = int(line[2])
walk = input().split()
ride = input().split()
inter = input().split()
for i in range(n):
    s += int(walk[i])
    s += (int(inter[i]) - ( s % int(inter[i]))) % int(inter[i])
    s += int(ride[i])
s += int(walk[n])
if s <= t:
    print("yes")
else:
    print("no")