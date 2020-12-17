class Bangle:
    def __init__(self, deg, mnt, sec, direc):
        self.deg = deg
        self.mnt = mnt
        self.sec = sec
        self.direc = direc
    
    def BearToAz(self):
        decimalDegrees = self.deg + ((self.mnt + (self.sec/float(60)))/float(60))
        if self.direc == "NE":
            return decimalDegrees
        if self.direc == "SE":
            return 180 - decimalDegrees
        if self.direc == "SW":
            return decimalDegrees + 180
        if self.direc == "NW":
            return 360 - decimalDegrees

    def BearingFormat(self):
        return self.direc[0] + str(self.deg) + "d" + str(self.mnt) + "'"\
            + str(self.sec) + '"' + self.direc[1]

### Main App ### 
import csv # This would be on top in a different page

# Loop where we ask user for input and 
while True:
    deg = int(input("Degree: "))
    mnt = int(input("Minute: "))
    sec = float(input("Seconds: "))
    direc = input("Direction: ")
    obj = Bangle(deg, mnt, sec, direc)
    azlist = []
    bearlist = []
    azlist.append(obj.BearToAz())
    bearlist.append(obj.BearingFormat())
    rows = [azlist[0],bearlist[0]]
    # Use methods defined to write to sequential file
    with open("Q2.csv", "a+") as f:
        writer = csv.writer(f)
        writer.writerow(rows)
    contvalue = input('continue?')
    if contvalue == "Yes":
        continue
    else:
        break

test = Bangle(45,30,00,"NE")
test2 = Bangle(34,33,36,"SW")
print(test.BearToAz())
print(test2.BearToAz())
print(test2.BearingFormat())