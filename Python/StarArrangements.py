n = int(input())
print(str(n) + ":")
for i in range(2, int((n + 3) / 2)):
    if (n % ((2 * i) - 1)) == 0:
        print(str(i) + "," + str(i - 1))
    elif (n % ((2 * i) - 1)) == i:
        print(str(i) + "," + str(i - 1))
    if n % i == 0:
        print(str(i) + "," + str(i))