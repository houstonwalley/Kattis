tot = 0
nums = {}
for i in range(10):
	n = int(input())
	n = n % 42
	if not n in nums:
		tot += 1
		nums[n] = 0
print(tot)
