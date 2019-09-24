import math
n = list(input().split())
theta = int(n[1])
h = int(n[0])
stheta = math.sin(math.radians(theta))
y = math.ceil(h / stheta)
print(y)