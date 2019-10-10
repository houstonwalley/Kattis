result = ''
for i in range(5):
    n = input()
    for j in range(len(n) - 2):
        if n[j] == 'F' and n[j + 1] == 'B' and n[j + 2] == 'I':
            result += str(i + 1) + ' '
if result == '':
    print('HE GOT AWAY!')
else:
    print(result)