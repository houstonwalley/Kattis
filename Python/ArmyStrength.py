t = int(input())
result = ''
for i in range(t):
	yeet = input()
	yeet = input().split()
	g = int(yeet[0])
	m = int(yeet[1])
	god = input().split()
	mech = input().split()
	go = []
	me = []
	for s in god:
		go.append(int(s))
	for s in mech:
		me.append(int(s))
	go.sort()
	me.sort()
	while True:
		if len(go) == 0:
			result += 'MechaGodzilla\n'
			break
		if len(me) == 0:
			result += 'Godzilla\n'
			break
		if go[0] >= me[0]:
			me.pop(0)
		else :
			go.pop(0)

print(result)
