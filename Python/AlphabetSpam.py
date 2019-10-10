cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = input()
wtot = 0
ltot = 0
ctot = 0
stot = 0
for i in range(len(n)):
    if n[i] == '_':
        wtot += 1
    elif n[i] in low:
        ltot += 1
    elif n[i] in cap:
        ctot += 1
    else:
        stot += 1
print(float(wtot / len(n)))
print(float(ltot / len(n)))
print(float(ctot / len(n)))
print(float(stot / len(n)))