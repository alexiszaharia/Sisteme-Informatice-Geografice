import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "t:/ie/bd_ro.mdb"

tab_lin = arcpy.GetParameterAsText(0)
exp_sel = arcpy.GetParameterAsText(1)

arcpy.SelectLayerByAttribute_management(tab_lin,"NEW_SELECTION", exp_sel )
arcpy.SelectLayerByLocation_management("localitati","WITHIN_A_DISTANCE",tab_lin,"2000 Meters","NEW_SELECTION")
arcpy.MakeFeatureLayer_management("localitati", "loc_layer", " tip <> 5  ")
arcpy.CopyFeatures_management("loc_layer","tab_loc_sel")
arcpy.SelectLayerByAttribute_management("localitati","CLEAR_SELECTION")
arcpy.MakeFeatureLayer_management(tab_lin, "linie_layer")
arcpy.CopyFeatures_management("linie_layer","tab_lin_sel")
arcpy.SelectLayerByAttribute_management(tab_lin,"CLEAR_SELECTION")

