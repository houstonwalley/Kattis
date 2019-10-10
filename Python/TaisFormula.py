n = int(input())
tot = 0
time = []
sam = []
for i in range(n):
    x = list(input().split())
    time.append(int(x[0]))
    sam.append(float(x[1]))
for i in range(n - 1):
    tot += ((sam[i] + sam[i + 1]) / 2) * (time[i + 1] - time[i]) / 1000
print(tot)