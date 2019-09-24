cont = []
for i in range(5):
    test = list(input().split())
    tot = 0
    for j in range(4):
        tot += int(test[j])
    cont.append(tot)
bigBoy = 0
for i in range(5):
    if cont[i] > cont[bigBoy]:
        bigBoy = i
print(str(bigBoy + 1) + " " + str(cont[bigBoy]))