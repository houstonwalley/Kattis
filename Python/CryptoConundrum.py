n = input()
tot = 0
for i in range(0, len(n), 3):
    count = 0
    if not n[i] == 'P':
        count += 1
    if not n[i + 1] == 'E':
        count += 1
    if not n[i + 2] == 'R':
        count += 1
    tot += count
print(tot)