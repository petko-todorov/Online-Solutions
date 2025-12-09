temps = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    temps.append(t)

if not temps:
    print(0)
else:
    lowest_temp = min(temps, key=lambda x: (abs(x), x < 0))
    print(lowest_temp)
