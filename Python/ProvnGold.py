n = list(input().split())
gold = int(n[0])
sil = int(n[1])
cop = int(n[2])
power = (gold * 3) + (sil * 2) + (cop * 1)
if power < 2:
    print("Copper")
elif power == 2:
    print("Estate or Copper")
elif power == 3 or power == 4:
    print("Estate or Silver")
elif power == 5:
    print("Duchy or Silver")
elif power > 5 and power < 8:
    print("Duchy or Gold")
elif power >= 8:
    print("Province or Gold")
