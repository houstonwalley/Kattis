import math

l = input().split()
d = float(l[0])
n = int(l[1])
result = ''

while not (d == 0.0 and n == 0):
	x_coord = []
	y_coord = []
	sors = []

	for i in range(n):
		sors.append(False)		

	for i in range(n):
		l = input().split()
		x_coord.append(float(l[0]))
		y_coord.append(float(l[1]))

	for i in range(len(x_coord)):
		for j in range(i + 1, len(x_coord)):
			dist = math.hypot((x_coord[i] - x_coord[j]), (y_coord[i] - y_coord[j]))
			if d > dist:
				sors[i] = True
				sors[j] = True

	sour = 0
	sweet = 0
	for s in sors:
		if s:
			sour += 1
		else:
			sweet += 1

	result += f'{sour} sour, {sweet} sweet\n'			

	l = input().split()
	d = float(l[0])
	n = int(l[1])

print(result)
