# Cleans up a string with repeating values in a sequence 
# List for testing without csv
# lst = [24,24,27,23,55,98,98,61,23,23,24,24]

import csv

# Need a list for the csv 
lst = []

file = open('sequence.csv','r')

for row in file:
    item = row.split(",")
    # List comprehension, does int(i) for every item inside the lst
    lst = [int(i) for i in item]
    print(lst)

file.close()

i = 0

# If lst has something 
if lst:
    # While counter i is less than the last item in the sequence
    while i < len(lst)-1:
        # If the index lst i is equal to the next index 
        if lst[i] == lst[i+1]:
            # Delete the index at list
            del lst[i]

        # Else you add 1 to the counter i to keep iterating
        else:
            i += 1 

# Proof that no consequetive sequence is repeated
print(lst)