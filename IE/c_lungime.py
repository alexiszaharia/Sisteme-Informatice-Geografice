import arcpy
import arcpy.da as da
import arcpy.mapping as harta

arcpy.env.workspace = "t:/IE/bd_ro.mdb"
arcpy.env.overwriteOutput = True

tab_inj = arcpy.GetParameterAsText(0)
tab_ind = arcpy.GetParameterAsText(1)

dh = harta.MapDocument("CURRENT")
df = harta.ListDataFrames(dh, "Layers")[0]

ljt = harta.Layer(tab_inj)
ljt.showLabels = True
harta.AddLayer(df, ljt, "TOP")

llt = harta.Layer(tab_ind)
harta.AddLayer(df, llt, "TOP")

listJud = [rand[0] for rand in da.SearchCursor("judTab", ("sj"))]

for jud in listJud:
     arcpy.SelectLayerByAttribute_management(ljt, "NEW_SELECTION","sj='"+jud+"'")
     arcpy.Clip_analysis(llt, ljt, "tabClip")
     arcpy.SelectLayerByAttribute_management(ljt, "CLEAR_SELECTION")
     listSeg = [rd[0] for rd in da.SearchCursor("tabClip", ("SHAPE@LENGTH"))]
     sl = sum(listSeg)
     crs = da.UpdateCursor(ljt, ("Lungime"), "sj='"+jud+"'" )
     rand = crs.next()
     rand[0] = sl
     crs.updateRow(rand)
del crs
