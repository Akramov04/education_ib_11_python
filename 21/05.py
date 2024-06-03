import datetime as dt
import math
birth = list(map(int, input().split(".")))
birth = dt.date(birth[2], birth[1], birth[0])
now = list(map(int, input().split(".")))
now = dt.date(now[2], now[1], now[0])

days_passed = (now - birth).days
physical_bior = math.sin((2 * math.pi * days_passed) / 23) * 100
emotional_bior = math.sin((2 * math.pi * days_passed) / 28) * 100
intellectual_bior = math.sin((2 * math.pi * days_passed) / 33) * 100

print(round(physical_bior, 2))
print(round(emotional_bior, 2))
print(round(intellectual_bior, 2))