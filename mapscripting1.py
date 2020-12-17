# Add layer to top of map from layers

import arcpy

# File paths are hard coded, not going to worry about the environment right now
aprx = arcpy.mp.ArcGISProject(r"D:\GEOM67PSP\Submissions\Assignment2\Question5.aprx")

# Ideally this should be on variable, we did cities.lyrx and country.lyrx just to see if it would work
cities = r"D:\GEOM67PSP\Submissions\Assignment2\cities.lyrx"
countries = r"D:\GEOM67PSP\Submissions\Assignment2\country.lyrx"
# inlayer = arcpy.mp.LayerFile(r"D:\GEOM67PSP\Submissions\Assignment2\cities.lyrx")
inlayer = arcpy.mp.LayerFile(cities) # Subjected to change depending on your layer
alayer = cities

# List layers
map = aprx.listMaps()[0]

# Describing feature with arcpy.Describe and shapetype (because it is a layer file)
# If points, top of the map
if arcpy.Describe(alayer).shapeType == "Point" or arcpy.Describe(cities).shapeType =="Multipoint":
    referencelayer = map.listLayers()[0]
    map.insertLayer(referencelayer, inlayer, "BEFORE")

# If lines then move added before/after lines
elif arcpy.Describe(alayer).shapeType == "Polyline":
    for layr in map.listLayers():

        desc = arcpy.Describe(layr)
        if desc.shapeType == "Polyline":
            referencelayer = layr
            break
    map.insertLayer(referencelayer, inlayer, "BEFORE")

# If polygons, move after polygon
elif arcpy.Describe(alayer).shapeType == "Polygon":
    for layr in map.listLayers():
        
        # If polygon, we continue with the code
        desc = arcpy.Describe(layr)
        if desc.shapeType == "Polygon":
            referencelayer = layr
            break
    map.insertLayer(referencelayer, inlayer, "BEFORE")

aprx.save()