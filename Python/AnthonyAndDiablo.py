import math

n = list(input().split())
a = float(n[0])
n = float(n[1])

d = n / math.pi
r = d /2
if math.pi * (r**2) >= a:
	print('Diablo is happy!')
else:
	print('Need more materials!')
