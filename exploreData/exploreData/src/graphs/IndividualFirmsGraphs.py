'''
Created on 13 feb. 2019

@author: javie
'''

import os
tmpDir = "C:/Users/javie/OneDrive - AUSTRAL/Investigación - JGS/Sudden Stop - Phoenix Miracle II - PHX (2)/Model/Python/Data/" 
os.chdir(tmpDir)
del tmpDir

import seaborn as sns
import numpy as np
import pandas as pd


# Read Data Files
fileID = "1F"

FirmsFile = 'Firms.' + fileID + ".csv"
Firms = pd.read_csv(FirmsFile)
del FirmsFile

ConsumersFile ='Consumers.' + fileID + ".csv"
Consumers = pd.read_csv(ConsumersFile)
del ConsumersFile

del fileID

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

# Define ploting functions

def firmsPlot(df, runs, varsToDraw, facet_kws = {}, cols = 5, rows = 3):

    if 'ExpectedLimit' in varsToDraw: df = joinLimits(df)
    
    fk = dict(sharey=False)
    fk.update(facet_kws)

    argsPlot = {'x': "tick",
                'y': "value",
                'col': "variable",
                'hue' : "FirmID",
                'kind' : "line",
                'facet_kws' : facet_kws
                }
    
    sns.set()
    sns.set_context("poster")

    if len(runs) == 1:
        firmsOneRunPlot(df, runs, varsToDraw, argsPlot, cols)
    elif len(varsToDraw) == 1:
        firmsOneVarPlot(df, runs, varsToDraw, argsPlot, cols)
    else:
        firmsMultiPlot(df, runs, varsToDraw, argsPlot, cols, rows)

    return

def firmsOneRunPlot(df, run, varsToDraw, argsPlot, cols):

    tmpDF = df[df.run==run[0]].loc[:, ['tick','FirmID'] + varsToDraw]

    tmpDF = tmpDF.melt(id_vars=['tick','FirmID'], value_vars = varsToDraw)

    cols = min(cols, len(varsToDraw))

    argsPlot.update({'data' : tmpDF, 'col_wrap' : cols })

    sns.relplot(**argsPlot)
    
    return

def firmsOneVarPlot(df, runs, varsToDraw, argsPlot, cols):

    tmpDF = df.loc[df.run.isin(runs), ['run','tick','FirmID'] + varsToDraw]

    argsPlot.update({'y' : varsToDraw[0], 
                     'col' : "run",
                     'data' : tmpDF,
                     'col_wrap' : cols
                     })        
        
    sns.relplot(**argsPlot)

    return

def firmsMultiPlot(df, runs, varsToDraw, argsPlot, cols, rows):

    #Truncate runs and vars to proper size
    runs = runs[:cols]
    varsToDraw = varsToDraw[:rows]

    tmpDF = df.loc[df.run.isin(runs), ['run','tick','FirmID'] + varsToDraw]
    tmpDF = tmpDF.melt(id_vars=['run','tick','FirmID'], value_vars = varsToDraw)

    argsPlot.update({'col' : 'run', 'row' : 'variable', 'data' : tmpDF})
    sns.relplot(**argsPlot)

    return

# firmsPlot(Firms, range(1, 5), ["Price","Quality",'ExpectedLimit'])

sns.jointplot(x="Price",y="Quality", data= Firms[Firms.tick==50],kind="kde")
sns.jointplot(x="ExpectedLowLimit",y="Quality", data= Firms[Firms.tick==50],kind="kde")
sns.jointplot(x="Demand",y="Quality", data= Firms[Firms.tick==50],kind="kde")
