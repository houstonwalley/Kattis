import math

n = int(input())
result =''
for i in range(n):
    safe = True
    f = list(input().split())
    velocity = float(f[0])
    theta = float(f[1])
    dist = float(f[2])
    h1 = float(f[3])
    h2 = float(f[4])
    thetad = math.radians(theta)

    time = dist / (velocity * math.cos(thetad))

    h = (velocity * time * math.sin(thetad)) - (.5 * 9.81 * (time**2))
    if not (h1 + 1 < h < h2 - 1):
        safe = False

    if result == '':
        if safe:
            result += 'Safe'
        else:
            result += 'Not Safe'
    else:
        if safe:
            result += '\nSafe'
        else:
            result += '\nNot Safe'

print(result)