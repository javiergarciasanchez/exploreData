'''
Created on 13 feb. 2019

@author: javie
'''

import seaborn as sns
import numpy as np
import pandas as pd

# Read Data Files
def readDataFiles(fileID = "20F"):

    import os
    path = "C:\\Users\javie\OneDrive - AUSTRAL\\Investigación - JGS\\Sudden Stop - Phoenix Miracle II - PHX (2)\\Model\\Python\\Data"    
    os.chdir(path)
    
    FirmsFile = 'Firms.' + fileID + ".csv"
    Firms = pd.read_csv(FirmsFile)
    del FirmsFile

    ConsumersFile ='Consumers.' + fileID + ".csv"
    Consumers = pd.read_csv(ConsumersFile)
    del ConsumersFile

    del fileID
    
    return [Firms, Consumers]

#replace 'Infinity' as higher limit and join lolimit and hilimit to draw a range
def joinLimits(df):

    #Replace 'Infinity'
    retval = df.copy()
    retval.loc[retval.ExpectedHighLimit == 'Infinity', 'ExpectedHighLimit'] = max(retval.ExpectedLowLimit) * 1.5
    retval["ExpectedHighLimit"] = retval["ExpectedHighLimit"].apply(pd.to_numeric)

    dfL = retval.rename(columns = {"ExpectedLowLimit":"ExpectedLimit"})
    dfL.drop('ExpectedHighLimit', axis = 1, inplace = True)

    retval.rename(columns = {"ExpectedHighLimit":"ExpectedLimit"}, inplace = True)
    retval.drop('ExpectedLowLimit', axis = 1, inplace = True)

    return retval.append(dfL)


# Percentile grouping
def groupByPerc(df_passed, var , var_lab, bins = 3):

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


# Define ploting functions

def firmsPlot(df, runs, varsToDraw, firmGroup = "FirmID", facet_kws = {}, cols = 5, rows = 3):

    if 'ExpectedLimit' in varsToDraw: df = joinLimits(df)
    
    fk = dict(sharey=False)
    fk.update(facet_kws)

    argsPlot = {'x': "tick",
                'y': "value",
                'col': "variable",
                'hue' : firmGroup,
                'kind' : "line",
                'facet_kws' : facet_kws
                }
    
    sns.set()
    sns.set_context("poster")

    if len(runs) == 1:
        firmsOneRunPlot(df, runs, varsToDraw, firmGroup, argsPlot, cols)
    elif len(varsToDraw) == 1:
        firmsOneVarPlot(df, runs, varsToDraw, firmGroup, argsPlot, cols)
    else:
        firmsMultiPlot(df, runs, varsToDraw, firmGroup, argsPlot, cols, rows)

    return

def firmsOneRunPlot(df, run, varsToDraw, firmGroup, argsPlot, cols):

    tmpDF = df[df.run==run[0]].loc[:, ['tick', firmGroup] + varsToDraw]

    tmpDF = tmpDF.melt(id_vars=['tick', firmGroup], value_vars = varsToDraw)

    cols = min(cols, len(varsToDraw))

    argsPlot.update({'data' : tmpDF, 'col_wrap' : cols })

    sns.relplot(**argsPlot)
    
    return

def firmsOneVarPlot(df, runs, varsToDraw, firmGroup, argsPlot, cols):

    tmpDF = df.loc[df.run.isin(runs), ['run','tick', firmGroup] + varsToDraw]

    argsPlot.update({'y' : varsToDraw[0], 
                     'col' : "run",
                     'data' : tmpDF,
                     'col_wrap' : cols
                     })        
        
    sns.relplot(**argsPlot)

    return

def firmsMultiPlot(df, runs, varsToDraw, firmGroup, argsPlot, cols, rows):

    #Truncate runs and vars to proper size
    runs = runs[:cols]
    varsToDraw = varsToDraw[:rows]

    tmpDF = df.loc[df.run.isin(runs), ['run','tick', firmGroup] + varsToDraw]
    tmpDF = tmpDF.melt(id_vars=['run','tick', firmGroup], value_vars = varsToDraw)

    argsPlot.update({'col' : 'run', 'row' : 'variable', 'data' : tmpDF})
    sns.relplot(**argsPlot)

    return

# firmsPlot(Firms, range(1, 5), ["Price","Quality",'ExpectedLimit'])

#sns.jointplot(x="Price",y="Quality", data= Firms[Firms.tick==50],kind="kde")
#sns.jointplot(x="ExpectedLowLimit",y="Quality", data= Firms[Firms.tick==50],kind="kde")
#sns.jointplot(x="Demand",y="Quality", data= Firms[Firms.tick==50],kind="kde")
