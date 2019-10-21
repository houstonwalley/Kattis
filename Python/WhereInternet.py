def union(parents, x, y):
	parent_x = find(parents, x)
	parent_y = find(parents, y)
	parents[parent_y] = parents[parent_x]	


def find(parents, i):
	if parents[i] == i:
		return i
	parents[i] = find(parents, parents[i])
	return parents[i]


t = input().split()
n = int(t[0])
m = int(t[1])
houses = []

for i in range(n):
	houses.append(i)

for j in range(m):
	t = input().split()
	one = int(t[0])
	two = int(t[1])

	if one < two:
		union(houses, one - 1, two - 1)
	else:
		union(houses, two - 1, one - 1)

result = ''
for i in range(n):
	if not find(houses, i) == find(houses, 0):
		result += str(i + 1) + '\n'

if result == '':
	print('Connected')
else:
	print(result)
