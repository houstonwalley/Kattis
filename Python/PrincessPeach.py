l = input().split()
n = int(l[0])
y = int(l[1])
missed = []
count = 0
for i in range(y):
	ln = int(input())
	if ln not in missed:
		count += 1
		missed.append(ln)

for i in range(n):
	if i not in missed:
		print(i)

print('Mario got ' + str(count) + ' of the dangerous obstacles.')
