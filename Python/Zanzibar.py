n = int(input())
result = ''
for i in range(n):
	l = input().split()
	dif = 0
	for i in range(len(l) - 1):
		if l[i + 1] == '0':
			break
		fir = int(l[i])
		sec = int(l[i + 1])
		if sec - (2 * fir) > 0:
			dif += sec - (2 * fir)
	result += str(dif) + '\n'
print(result)
