# -*- coding: utf-8 -*-


import seaborn as sns
import numpy as np
import pandas as pd

def setScenariosToData(data, param, scenTab):
    
    runsXScen = pd.DataFrame(columns = ['run','scenario'])
    
    for i, s in scenTab.iterrows():        
        runsXScen = runsXScen.append(Param.loc[eval(scenarios[i])].assign(scenario = scen_lab[i]))

    return data.merge(scen, on='run')

#ret = getScenarios(F, Param,\
#        ["(round(df.qualityDiscountMostLikely, 3) == 0.999) & (round(df.qualityDiscountMean, 3) == 0.998)", \
#             "(round(df.qualityDiscountMostLikely, 3) == 0.9) & (round(df.qualityDiscountMean, 3) == 0.8)"],\
#       ["sin_disc","con_disc"])

# Get Scenarios
# Parameters
#
# scenarios = ["(round(df.qualityDiscountMostLikely, 3) == 0.999) & (round(df.qualityDiscountMean, 3) == 0.998)", \
#             "(round(df.qualityDiscountMostLikely, 3) == 0.9) & (round(df.qualityDiscountMean, 3) == 0.8)"]
#
# scen_lab = ["sin_disc","con_disc"]
    

def getScenarios(data, Param, scenarios , scen_lab):
    
    retval = data.copy()
    
    scen = pd.DataFrame(columns = ['run','scenario'])
    
    for i in range(len(scenarios)):        
        scen = scen.append(Param.loc[eval(scenarios[i])].assign(scenario = scen_lab[i]))

    retval = retval.merge(scen, on='run')
    
    return retval

# =============================================================================
# Creates a Table of the Scenarios in a Run
# Row with unwanted scenarios should be droped
# Scenarios should be added names and label for plotting
# 
# =============================================================================
def getScenariosTable(param):

    paramTab = pd.DataFrame(([""],[""]), columns= ['name','label'])
    
    relevantParam = []

    for c in param.columns:
    
        if (c != 'run') & (c != 'randomSeed'):

            flatParam = param.loc[:,c].unique()
    
            if len(flatParam) > 1:
                relevantParam = relevantParam.append(pd.DataFrame(data = flatParam, columns=[c]))
    
    paramTab = paramTab.assign(key=1)
    for p in relevantParam:
        p = p.assign(key=1)
        paramTab = paramTab.merge(p, on='key', how='outer')
    
    paramTab = paramTab.drop(columns=['key'])
    
    return paramTab

# Get raw Scenarios
def getRawScenarios(param):

    paramSet = dict()

    for c in param.columns:
    
        if (c != 'run') & (c != 'randomSeed'):

            flatParam = param.loc[:,c].unique()
    
            if len(flatParam) > 1:
                paramSet.update({c : flatParam})
    
    return paramSet    
            
# Percentile grouping
def setPercetile(df_passed, var , var_lab, bins = 3):

    df = df_passed.copy()
    
    mRun = int(max(df.run))
    
    gdf = pd.DataFrame(columns= ["run","FirmNumID", "G_" + var_lab])

    lab =list(map(lambda x : var_lab + '_' + str(x), range(1,bins+1)))
    
    for r in range(1, mRun + 1):
        
        rDF = df.loc[(df.run == r) & (df.tick == 1),["run","FirmNumID", var]]
        rDF['G_' + var_lab] = pd.qcut(rDF.loc[:, var], bins, labels = lab)       
        gdf = gdf.append(rDF.drop(columns=var))
 
    df = df.merge(gdf, how = "left", on = ["run", "FirmNumID"])

    return df
