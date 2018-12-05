import arcpy
import arcpy.da as da
import arcpy.mapping as harta

arcpy.env.workspace = "t:/IE/bd_ro.mdb"
arcpy.env.overwriteOutput = True

dh = harta.MapDocument("CURRENT")
df = harta.ListDataFrames(dh, "Layers")[0]

arcpy.AddField_management("judTab", "pondere", "LONG")

lval = [rd[0] for rd in da.SearchCursor("judTab", "lungime")]
slung = sum(lval)

with da.UpdateCursor("judTab", ("lungime", "pondere")) as crs:
     for rd in crs:
         rd[1] = int (round (rd[0] / slung * 100))
         crs.updateRow(rd)

del crs
