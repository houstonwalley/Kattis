n = list(input().split())
hands = int(n[0])
domsuit = n[1]
tot = 0
num = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7']
dom = [11, 4, 3, 20, 10, 14, 0, 0]
nondom = [11, 4, 3, 2, 10, 0, 0, 0]
for i in range(hands * 4):
    h = str(input())
    value = h[0]
    suit = h[1]
    for j in range(len(num)):
        if num[j] == value:
            if suit == domsuit:
                tot += dom[j]
            else:
                tot += nondom[j]
            break
print(tot)