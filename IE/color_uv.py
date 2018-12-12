import arcpy
import arcpy.da as da

arcpy.AddField_management("judTab", "pondere", "SHORT")
lista_lungimi = [rand[0] for rand in da.SearchCursor("judTab", ("lungime"))]
sl=sum(lista_lungimi)
with da.UpdateCursor("judTab", ("lungime", "pondere")) as Calc_pondere:
     for rand in Calc_pondere:
         rand[1] = int (round (rand[0] / sl * 100))
	 if rand[1]==0:
	 	rand[1]=1
         Calc_pondere.updateRow(rand)

dh = harta.MapDocument("CURRENT")
df = harta.ListDataFrames(dh, "Layers")[0]

l_jud_sel = harta.ListLayers(dh,"judTab",df)[0]
fl_simb = "T:/IE/uvc.lyr"
l_simb = harta.Layer(fl_simb)
harta.UpdateLayer(df, l_jud_sel, l_simb, "TRUE")
if l_jud_cel.symbologyType == "UNIQUE_VALUES":
	l_jud_cel.symbology.valueField = "pondere"
	l_jud_cel.symbology.addAllValues()
	l_jud_cel.symbology.showOtherValues = false

arcpy.RefreshActiveView()
arcpy.RefreshTOC()
