n = list(input().split())
k = int(n[1])
if not int(n[0]) > (2**k):
    print('Your wish is granted!')
else:
    print('You will become a flying monkey!')