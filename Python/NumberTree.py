n = input().split()
h = int(n[0])
leng = (2**(h + 1)) - 1
if len(n) == 1:
	print(leng)
	exit(0)
dir = n[1]
i = 1
for s in dir:
	if s == 'L':
		i = 2 * i
	else:
		i = (2 * i) + 1
print(leng - i + 1)
