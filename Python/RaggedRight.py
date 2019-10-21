leng = []
try:
	while True:
		line = input()
		if len(line) > 0:
			leng.append(len(line))
		else:
			break
except EOFError:
	pass

big = 0
for i in range(len(leng)):
	if leng[i] > big:
		big = leng[i]

tot = 0
for i in range(len(leng) - 1):
	tot += (big - leng[i])**2

print(tot)
	
