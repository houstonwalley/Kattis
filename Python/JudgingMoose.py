n = list(input().split())
x = int(n[0])
y = int(n[1])
if x == 0 and y == 0:
	print('Not a moose')
else:
	t = max(x, y)
	f = t * 2
	if t == x and t == y:
		print('Even ' + str(f))
	else:
		print('Odd ' + str(f))
