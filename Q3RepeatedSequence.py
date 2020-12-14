# cleans up a string with repeating values

csv = [24,24,27,23,55,98,98,61,23,23,24,24]

# def CleanRp():

a = 0
b = 1


print (csv[a])
# print (csv[b])

while True:
    # print(a,b)
    a = a+1
    # b = b+1
    if csv[a] == csv[-1]:
        break

if csv[a] == csv[b]:
    csv.pop(a)

print(csv)