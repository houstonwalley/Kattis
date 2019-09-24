import math
n = list(input().split())
x = int(n[0])
y = int(n[1])
x1 = int(n[2])
y1 = int(n[3])
x2 = int(n[4])
y2 = int(n[5])
dx = min(abs(x - x1), abs(x - x2))
dy = min(abs(y - y1), abs(y - y2))
if x1 < x < x2:
    dx = 0
if y1 < y < y2:
    dy = 0
print(math.sqrt(pow(dx, 2) + pow(dy, 2)))