n = str(input())
hiss = False
for i in range(len(n) - 1):
    if n[i] == "s" and n[i + 1] == "s":
        hiss = True
if hiss:
    print("hiss")
else:
    print("no hiss")