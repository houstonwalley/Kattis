
col = {}
n = int(input())
for i in range(n):
	lineIn = input().split()

	try:
		radius = int(lineIn[1])
		col[radius] = lineIn[0]
	except ValueError:
		radius = (int(lineIn[0]) / 2)
		col[radius] = lineIn[1]

for key in sorted(col):
	print(col[key])
	
