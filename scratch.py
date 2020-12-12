import math

azimuth = 100.200
split = math.modf(azimuth)
# print(split[1], split[0])
split2 = math.modf(split[0]*60)
deg = split[1]
min = split[0]
sec = split2[0]
print(int(deg),int(min),int(sec))