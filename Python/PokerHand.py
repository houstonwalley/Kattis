n = list(input().split())
rank = []
num = []
for s in range(5):
	yeet = n[s]
	if yeet[0] in rank:
		for i in range(len(rank)):
			if yeet[0] == rank[i]:
				num[i] += 1
	else:
		rank.append(yeet[0])
		num.append(1)
print(max(num))
