miles = float(input())
n = (((miles * 5280) / 4854) * 1000)
if n % 1 >= .5:
    n += 1
print(int(n))