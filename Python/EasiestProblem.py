n = str(input())
result = ''
while not n == '0':
    sum_dig = 0
    for i in range(len(n)):
        sum_dig += int(n[i])
    k = 11
    pro = str(k * int(n))
    mul_dig = 0
    for i in range(len(pro)):
        mul_dig += int(pro[i])
    k = 12
    while not mul_dig == sum_dig:
        pro = str(k * int(n))
        mul_dig = 0
        for i in range(len(pro)):
            mul_dig += int(pro[i])
        k += 1
    result += str(k - 1) + '\n'
    n = str(input())
print(result)