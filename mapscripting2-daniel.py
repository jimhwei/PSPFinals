import arcpy
# ft_name = input('give name')        # this will be fc
# symb_type = input('give style')     # symbology type
# symb_field = input('give field')
# classes = int(input('give number'))
ft_name = 'feature_name'      # this will be fc
symb_type = "Unique Values"   # symbology type
symb_field = 'testfield'
classes = 3

prj = arcpy.mp.ArcGISProject(r'C:\somepath\testproject.aprx')  # getting my project object
ref_lyr1 = r'C:\somepath\ref1.lyr'   # Graduated Colour
ref_lyr2 = r'C:\somepath\ref2.lyr' # Unique Values
ref_lyr3 = r'C:\somepath\ref3.lyr' # Graduated Symbol

if symb_type == 'Unique Values':
    ref_lyr = ref_lyr2
elif symb_type == 'Graduated Colour':
    ref_lyr = ref_lyr1
elif symb_type == 'Graduated Symbol':
    ref_lyr = ref_lyr3

for m in prj.listMaps():
    if m.listLayers(ft_name)[0] == ft_name:
        lyr_variable = m.listLayers(ft_name)[0]
arcpy.ApplySymbologyFromLayer_management(lyr_variable, ref_lyr)
sym = lyr_variable.symbology
sym.updateRenderer('UniqueValueRenderer')
sym.renderer.fields = [symb_field]
lyr_variable.symbology = sym