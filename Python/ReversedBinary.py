def to_binary(n):
    result = ''
    for i in range(30, -1, -1):
        if n >= 2**i:
            n -= 2**i
            result += '1'
        else:
            result += '0'
    return result


def flip_bin(s):
    result = ''
    one = False
    for i in range(len(s)):
        if one:
            result += s[i]
        elif s[i] == '1':
            result += '1'
            one = True
    return result


def bin_to_dec(x):
    tot = 0
    for i in range(len(x)):
        if x[i] == '1':
            tot += 2**i
    return tot

l = int(input())
print(bin_to_dec(flip_bin(to_binary(l))))
