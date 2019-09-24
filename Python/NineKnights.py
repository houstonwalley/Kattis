row1 = str(input())
row2 = str(input())
row3 = str(input())
row4 = str(input())
row5 = str(input())
valid = True
k = 'k'
for i in range(3):
    if row1[i] == k and row2[i + 2] == k:
        valid = False
        break
    if row2[i] == k and row1[i + 2] == k:
        valid = False
        break
    if row2[i] == k and row3[i + 2] == k:
        valid = False
        break
    if row3[i] == k and row2[i + 2] == k:
        valid = False
        break
    if row3[i] == k and row4[i + 2] == k:
        valid = False
        break
    if row4[i] == k and row3[i + 2] == k:
        valid = False
        break
    if row4[i] == k and row5[i + 2] == k:
        valid = False
        break
    if row5[i] == k and row4[i + 2] == k:
        valid = False
        break
for i in range(5):
    if not valid:
        break
    if i == 0:
        if row1[i] == k and row3[i + 1] == k:
            valid = False
            break
        if row2[i] == k and row4[i + 1] == k:
            valid = False
            break
        if row3[i] == k and row5[i + 1] == k:
            valid = False
            break
    elif i == 4:
        if row1[i] == k and row3[i - 1] == k:
            valid = False
            break
        if row2[i] == k and row4[i - 1] == k:
            valid = False
            break
        if row3[i] == k and row5[i - 1] == k:
            valid = False
            break
    else:
        if row1[i] == k and row3[i + 1] == k:
            valid = False
            break
        if row2[i] == k and row4[i + 1] == k:
            valid = False
            break
        if row3[i] == k and row5[i + 1] == k:
            valid = False
            break
        if row1[i] == k and row3[i - 1] == k:
            valid = False
            break
        if row2[i] == k and row4[i - 1] == k:
            valid = False
            break
        if row3[i] == k and row5[i - 1] == k:
            valid = False
            break
kcount = 0
for c in row1:
    if c == k:
        kcount += 1
for c in row2:
    if c == k:
        kcount += 1
for c in row3:
    if c == k:
        kcount += 1
for c in row4:
    if c == k:
        kcount += 1
for c in row5:
    if c == k:
        kcount += 1
if not kcount == 9:
    valid = False
if valid:
    print('valid')
else:
    print('invalid')