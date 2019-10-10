n = input().split()
result = ''
while not (n[0] == '0' and n[1] == '0' and n[2] == '0.0'):
    mowedx = True
    mowedy = True
    x = int(n[0])
    y = int(n[1])
    w = float(n[2])
    xmow = list(input().split())
    xmow.sort(key=float)
    countx = 0
    for i in range(len(xmow)):
        if i == 0 and ((float(xmow[i]) - (w / 2)) > 0):
            mowedx = False
            break
        elif (i == x - 1) and (float(xmow[i]) + (w / 2)) < 75:
            mowedx = False
            break
        elif (float(xmow[i]) - (w/2)) > (float(xmow[i - 1]) + (w / 2)):
            mowedx = False
            break
        else:
            countx += 1
    ymow = list(input().split())
    ymow.sort(key=float)
    county = 0
    for i in range(len(ymow)):
        if i == 0 and ((float(ymow[i]) - (w / 2)) > 0):
            mowedy = False
            break
        elif (i == y - 1) and (float(ymow[i]) + (w / 2)) < 100:
            mowedy = False
            break
        elif (float(ymow[i]) - (w/2)) > (float(ymow[i - 1]) + (w / 2)):
            mowedy = False
            break
        else:
            county += 1
    if county == y:
        mowedy = True
    if mowedx and mowedy:
        if result == '':
            result += 'YES'
        else:
            result += '\nYES'
    else:
        if result == '':
            result += 'NO'
        else:
            result += '\nNO'
    n = input().split()
print(result)