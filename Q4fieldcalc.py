# In ArcGIS Pro’s Calculate Field, create a programmer-defined function 
# and call the function passing in fields or values as parameters

# – Perform a python mathematical operation for each record using the values 
# in several fields (eg. max, min, sum, pow, sqrt, round, trig, degrees, radians, hypot, abs ).
# – Use string functions to rearrange the values from a field or 
# combine the values from several fields

############################################################

# C) 
# Given a table with an Area field and a Population field, 
# write a Python field calculate field script that determines the 
# population density class based on the ratio of population to area 
# for 4 different class ranges 
# (eg. > 50 is class 1, 30-50 is class 2, 15-30 is class 3, 0-15 is class 4)

# In ArcGIS Pro
# Class = CalculateField(!POP1991!, !AREA!)

# Code block
def CalculateField(population, area):

    exp = population/area

    if exp > 50:
        field = 1
    elif 30 < exp <= 50:
        field = 2
    elif 15 < exp <= 30:
        field = 3
    else:
        field = 4
    
    return field

############################################################

# Part B)
# Given a table with an address field consisting of number name type and 
# direction (eg. 195 Lindsay St N), write a Python calculate field script 
# that will replace the short form street type with 
# its full word (eg. Street instead of St)

def ReplaceShortForm(address):

    stradd = address.split(" ")

    if stradd[-2] == "St":
        stradd.replace("St", "Street")
    
    return stradd