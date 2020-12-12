def decdeg2dms(dd):
    mnt,sec = divmod(dd*3600,60)
    deg,mnt = divmod(mnt,60)
    print(deg,mnt,sec)
    return deg,mnt,sec

dd = 45 + 30.0/60 + 1.0/3600
print (dd)
decdeg2dms(dd)