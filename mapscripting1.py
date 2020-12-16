# Add layer to top of map from layers

import arcpy
# from arcpy import env
# import os
# cwd = os.getcwd()

aprx = arcpy.mp.ArcGISProject(r"D:\GEOM67PSP\Submissions\Assignment2\Question5.aprx")

cities = r"D:\GEOM67PSP\Submissions\Assignment2\cities.lyrx"
countries = r"D:\GEOM67PSP\Submissions\Assignment2\country.lyrx"
# inlayer = arcpy.mp.LayerFile(r"D:\GEOM67PSP\Submissions\Assignment2\cities.lyrx")
inlayer = arcpy.mp.LayerFile(countries)

# List layers
map = aprx.listMaps()[0]

# Describing feature with arcpy.Describe and shapetype (because it is a layer file)
# If points, top of the map
# if arcpy.Describe(cities).shapeType == "Point" or arcpy.Describe(cities).shapeType =="Multipoint":
#     referencelayer = map.listLayers()[0]
#     map.insertLayer(referencelayer, inlayer, "BEFORE")

# If lines then move added before/after lines
if arcpy.Describe(cities).shapeType == "Polyline":
    referencelayer = map.listLayers()[0]
    map.insertLayer(referencelayer, inlayer, "BEFORE")
else: 
    print("not a line")



# If polygons, move after polygon
if arcpy.Describe(countries).shapeType == "Polygon":
    for layr in map.listLayers():
        
        # If polygon, we continue with the code
        desc = arcpy.Describe(layr)
        if desc.shapeType == "Polygon":
            referencelayer = layr
            break
    map.insertLayer(referencelayer, inlayer, "BEFORE")
aprx.save()