n = input()
can = {}

name = []

while not n == '***':
	if n not in can:
		can[n] = 1
		name.append(n)
	else:
		can[n] = can[n] + 1
	n = input()

top = 0
winner = ''
for s in name:
	if can[s] > top:
		top = can[s]
		winner = s
time = 0
for s in name:
	if can[s] == top:
		time += 1
if time >= 2:
	print('Runoff!')
else:
	print(winner)
