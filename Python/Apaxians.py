n = input()
result = n[0]
for i in range(1, len(n)):
    if not n[i] == n[i - 1]:
        result += n[i]
print(result)