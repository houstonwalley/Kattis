import datetime
l = list(input().split())
x = int(l[0])
y = int(l[1])
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
yeet = datetime.date(2009, y, x).weekday()
print(day[yeet])
