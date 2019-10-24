n = input().split()
x = int(n[0])
y = int(n[1])
if (((x * 4) + (y * 3)) % 2) == 0:
	print('possible')
else:
	print('impossible')
