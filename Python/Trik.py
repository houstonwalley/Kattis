n = list(input())
x = 1

for i in range(len(n)):
    yee = n[i]
    if yee == 'A' and x == 1:
        x = 2
    elif yee == 'A' and x == 2:
        x = 1
    elif yee == 'B' and x == 2:
        x = 3
    elif yee == 'B' and x == 3:
        x = 2
    elif yee == 'C' and x == 1:
        x = 3
    elif yee == 'C' and x == 3:
        x = 1

print(x)
