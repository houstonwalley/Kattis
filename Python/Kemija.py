n = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
result = ''
for s in n:
	i = 0
	while i < len(s):
		result += s[i]
		if s[i] in vowels:
			i += 3
		else:
			i += 1
	result += ' '
print(result)
		 
