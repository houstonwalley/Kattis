n = int(input())
result = ''
lol =[]
while not n == 0:
    names = []
    for i in range(n):
        names.append(input())
    hell = []
    for j in names:
        if j[:2] not in hell:
            hell.append(j[:2])
    hell.sort()
    pop = ''
    for s in hell:
        for b in names:
            if s == b[:2]:
                if pop == '':
                    pop += b
                else:
                    pop += ' ' + b

    lol.append(pop)
    n = int(input())
for d in lol:
    r = d.split()
    for e in r:
        if result == '':
            result += e
        else:
            result += '\n' + e
    result += '\n'
print(result)