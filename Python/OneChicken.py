x = list(input().split())
n = int(x[0])
m = int(x[1])
if n < m:
    q = m - n
    if not q == 1:
        print('Dr. Chaz will have ' + str(q) + ' pieces of chicken left over!')
    else:
        print('Dr. Chaz will have ' + str(q) + ' piece of chicken left over!')
else:
    q = n - m
    if not q == 1:
        print('Dr. Chaz needs ' + str(q) + ' more pieces of chicken!')
    else:
        print('Dr. Chaz needs ' + str(q) + ' more piece of chicken!')