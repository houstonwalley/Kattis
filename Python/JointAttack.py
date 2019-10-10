numer = 0
denom = 0


def attack(i, x, numer, denom):
    if i == 0:
        numer = (int(x[i]) * denom) + numer
        return str(numer) + '/' + str(denom)
    elif i == n - 1:
        numer = 1
        denom = int(x[i])
        return attack(i - 1, x, numer, denom)
    else:
        numer = numer + (denom * int(x[i]))
        z = numer
        y = denom
        denom = z
        numer = y
        return attack(i - 1, x, numer, denom)


n = int(input())
x = list(input().split())
print(attack(n - 1, x, numer, denom))