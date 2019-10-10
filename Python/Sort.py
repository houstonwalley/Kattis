w = list(input().split())
x = list(input().split())
num = []
count = []
for s in x:
    if not s in num:
        num.append(s)
        count.append(1)
    else:
        for i in range(len(num)):
            if num[i] == s:
                count[i] += 1

result = ''
cap = int(w[0])
for i in range(len(num)):
    place = 0
    max = 0
    for j in range(len(num)):
        if count[j] > max:
            max = count[j]
            place = j
    for t in range(max):
        result += num[place] + ' '
    count[place] = 0

print(result)