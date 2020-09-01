testCases = int(input())
distances = []
for i in range(testCases):
	numStores = int(input())
	stores = input().split()
	stores = [int(j) for j in stores]
	stores.sort()
	min = stores[0]
	max = stores[numStores - 1]
	efficient = (max - min) * 2
	distances.append(efficient)
for n in distances:
	print(n)
