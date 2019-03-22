# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:53:32 2019

@author: javie
"""

#Process raw file
rawID =  "2019.mar..22.18_52_38"
newID = "SS4000"
renameFiles(rawID, newID)
f, p = readDataFiles(newID)
sc = createScenariosTable(p)

#Manually set scenarios names
sc
SS3 = setScenariosToData(f, p, sc)
del f, p, sc, rawID, newID

id_vars=["randomSeed","scenario","tick","FirmNumID"]
vars = ["Quality","Price","Demand","Profit","ExpectedLowLimit","DemandShare"]
SS3cDif = setDiferences(SS3, "SS", "NSS", vars)
SS3_Dif = SS3cDif[SS3cDif.scenario == "Dif"]

r = range(1,15)
pl(SS3, r, "Quality")
pl(SS3, r, "Demand")
pl(SS3, r, "DemandShare")
pl(SS3, r, "ExpectedLowLimit")

pl(SS3_Dif, r, "Quality")
pl(SS3_Dif, r, "Demand")
pl(SS3_Dif, r, "DemandShare")
pl(SS3_Dif, r, "ExpectedLowLimit")

plMelt(SS3, r, ["Quality","Demand"])

# Create SS3 with only lowest q firms
tmp = SS3.set_index(["randomSeed","scenario","tick"])
tmp["minQ"] = SS3.loc[:, ["randomSeed","scenario","tick","Quality"]].groupby(by=["randomSeed","scenario","tick"]).min()
SS3minQ = tmp[tmp.Quality == tmp.minQ].reset_index()
del tmp

SS3minQcDif = setDiferences(SS3minQ, "SS", "NSS", vars)
SS3minQ_Dif = SS3minQcDif[SS3minQcDif.scenario == "Dif"]
plMelt(SS3minQ_Dif, r, ["Quality","Demand","Profit"])
