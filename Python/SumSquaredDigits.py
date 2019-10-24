def ssd(b, n):
	result = 0
	if b >= 8:
		times = 12
	else:
		times = 32
	for i in range(times, -1, -1):
		count = 0
		while b**i <= n:
			n -= b**i
			count +=1
		result += count**2
	return result


p = int(input())
result = ''
for i in range(p):
	g = input().split()
	k = g[0]
	b = int(g[1])
	n = int(g[2])
	result += k + ' ' + str(ssd(b, n)) + '\n'
print(result)
