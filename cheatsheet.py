# Easy csv method 
import csv

fo = open('azimuths.csv', 'r')
for row in fo:
    item = row.split(",")
    print(row)
fo.close()

# Conver i in to integers
lst = [int(i) for i in item]

# math.modf method for splitting lines
import math

azimuth = 100.200
split = math.modf(azimuth)
# print(split[1], split[0])
split2 = math.modf(split[0]*60)
deg = split[1]
min = split[0]
sec = split2[0]
print(int(deg),int(min),int(sec))

# Altnerate csv method
# with open('azimuths.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     for row in csv_reader:
#         print(row)

# Advanced aligning method
# Example 1
print('L {:<20} R'.format('x'))
# Example 2
print('L {:^20} R'.format('x'))
# Example 3
print('L {:>20} R'.format('x'))