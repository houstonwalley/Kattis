n = int(input())

names = []

for i in range(n):
	m = int(input())
	name = str(input())
	pea_soup = False
	pancakes = False
	items = []
	for j in range(m):
		item = str(input())
		items.append(item)
	if 'pea soup' in items:
			pea_soup = True
	if 'pancakes' in items:
			pancakes = True
	if pea_soup and pancakes:
		print(name)
		exit()		


print('Anywhere is fine I guess')
