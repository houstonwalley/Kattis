n = int(input())
sentence = []
yeet = []
for i in range(n):
    fox = input().split()
    sounds = []
    y = input().split()
    while not y[0] == 'what':
        sounds.append(y[2])
        y = input().split()
    result = ''
    for s in fox:
        if s not in sounds:
            if result == '':
                result += s
            else:
                result += ' ' + s
    yeet.append(result)
for x in yeet:
    print(x)
