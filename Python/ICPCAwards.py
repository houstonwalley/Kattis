n = int(input())
uni = []
winner = []
for i in range(n):
	x = input()
	y = x.split()
	if y[0] not in uni:
		uni.append(y[0])
		winner.append(x)
for i in range(12):
	print(winner[i])
