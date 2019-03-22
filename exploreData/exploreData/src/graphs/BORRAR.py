# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:58:01 2019

@author: javie
"""

    
    
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
