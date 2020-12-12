# Reads a series of azimuths from a sequential file
import csv
import math
# Converts the azimuths to bearings (in decimal degrees)

# Use exceptions to validate file access
try: 
    # Opens file and prints a column header
    file = open('azimuths.csv', 'r')
    print ("Azimuth(dd)\tBearing(dd)\tBearing(dms)")
    
    # Iterates through the csv and split by ","
    for item in file:
        lst = item.split(",")
        lst = [float(i) for i in lst] # converts list items into float
        
        for azimuth in lst:
            minute,second = divmod(azimuth*3600,60)
            degree,minute = divmod(minute,60)
            degree, minute, second = int(degree), int(minute), int(second)

            # 0° – 90° is NE quadrant: bearing = azimuth
            if 0 <= degree <= 90:
                bearingdd = "N" + str(azimuth) + "E"
                bearingdms = "N" + str(degree) + "d" + str(minute) + "'" + str(second) + '"' +"E"

            # 90° – 180° is SE quadrant: bearing = 180° – azimuth or azimuth = 180 - bearing
            elif 90 < azimuth <=180:
                bearingdd = "S" + str(180 - azimuth) + "E"
                bearingdms = "S" + str(180 - degree) + "d" + str(minute) + "'" + str(second) + '"' + "E"
            
            # 180° – 270° is SW quadrant: bearing = azimuth – 180° or azimuth = bearing + 180
            elif 180 < azimuth <= 270:
                bearingdd = "S" + str(azimuth - 180) + "W"
                bearingdms = "S" + str(degree - 180) + "d" + str(minute) + "'" + str(second) + '"' + "W"
            
            # 270° – 360° is NW quadrant: bearing = 360° - azimuth or azimuth = 360 - bearing
            elif 270 < azimuth <= 360:
                bearingdd = "N" + str(360 - azimuth) + "W"
                bearingdms = "N" + str(360 - degree) + "d" + str(minute) + "'" + str(second) + '"' + "W"
            
            # If an invalid error exists
            else: 
                print ("Please enter azimuth between 0 - 360°")

            # Displays the azimuths and their corresponding bearings 
            # in columns with headers at the top of the column
            print (azimuth,'\t\t', bearingdd,'\t', bearingdms)

except TypeError:
    print("An error has occured")

file.close()