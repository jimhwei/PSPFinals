# Reads a series of azimuths from a sequential file
import csv
# Converts the azimuths to bearings (in decimal degrees)
# lst = [45.500000, 100.200000, 214.560000, 303.987654]
# Test Variables
# azimuth = 45.500000
# azimuth = 100.200000
# azimuth = 214.560000
# azimuth = 303.987654

with open('azimuths.csv') as csvfile: 
    lst = csv.reader(csvfile, delimiter=',')


print ("Azimuth(dd), Bearing(dd), Bearing(dms)")

for azimuth in lst:

    minute,second = divmod(azimuth*3600,60)
    degree,minute = divmod(minute,60)
    degree, minute, second = int(degree), int(minute), int(second)
    # print (degree,minute,second)

    try: 
        # 0° – 90° is NE
        # NE quadrant: bearing = azimuth
        if 0 <= degree <= 90:
            bearingdd = "N" + str(azimuth) + "E"
            bearingdms = "N" + str(degree) + "d" + str(minute) + "'" + str(second) + '"' +"E"

        # 90° – 180° is SE
        # SE quadrant: bearing = 180° – azimuth or azimuth = 180 - bearing
        elif 90 < azimuth <=180:
            bearingdd = "S" + str(180 - azimuth) + "E"
            bearingdms = "S" + str(180 - degree) + "d" + str(minute) + "'" + str(second) + '"' + "E"
        
        # 180° – 270° is SW
        # SW quadrant: bearing = azimuth – 180° or azimuth = bearing + 180
        elif 180 < azimuth <= 270:
            bearingdd = "S" + str(azimuth - 180) + "W"
            bearingdms = "S" + str(degree - 180) + "d" + str(minute) + "'" + str(second) + '"' + "W"
        
        # # 270° – 360° is NW
        # # NW quadrant: bearing = 360° - azimuth or azimuth = 360 - bearing
        elif 270 < azimuth <= 360:
            bearingdd = "N" + str(360 - azimuth) + "W"
            bearingdms = "N" + str(360 - degree) + "d" + str(minute) + "'" + str(second) + '"' + "W"
        else: 
            print ("Please enter azimuth between 0 - 360°")

        print (azimuth, bearingdd, bearingdms)

    except TypeError:
        print("Something incorrectly was put in")


# Displays the azimuths and their corresponding bearings 
# in columns with headers at the top of the column

# Use exceptions to validate file access
# the azimuth values read from the file and include a general exception for unanticipated system errors.