n = int(input())
result = ''
count = 1
while not n == 0:
    result += 'SET ' + str(count) + '\n'
    words = []
    for i in range(n):
        x = input()
        words.append(x)
    for i in range(n):
        if i % 2 == 0:
            result += words[i] + '\n'
    for i in range(n - 1, -1, -1):
        if i % 2 == 1:
            result += words[i] + '\n'
    n = int(input())
    count += 1
print(result)