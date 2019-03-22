# -*- coding: utf-8 -*-
"""
Created on 13 feb. 2019

@author: javie
"""

import os
import pandas as pd
path = u"C:\\Users\javie\OneDrive - AUSTRAL\\Investigación - JGS\\Sudden Stop - Phoenix Miracle II - PHX (2)\\Model\\Python\\Data"    

# Rename Files
def renameFiles(oldN, newN):
    
    os.chdir(path)  

    for filename in os.listdir("."):
        newFN = filename.replace(oldN, newN)
        os.rename(filename, newFN)
        
    return

def readDataFiles(fileID = "20F", consumers=False):
    
    os.chdir(path)

    Firms = readFirmFile(fileID)
    Params = readParamFile(fileID)
    
    if consumers :
        Consumers = readConsumerFile(fileID)
        return [Firms, Consumers, Params]
    else:
        return [Firms, Params]

# Read Data Files
def readFirmFile(fileID = "20F"):
    
    FirmsFile = 'Firms.' + fileID + ".csv"
    Firms = pd.read_csv(FirmsFile)
    del FirmsFile
    
    del fileID
    
    return Firms

def readConsumerFile(fileID = "20F"):

    ConsumersFile ='Consumers.' + fileID + ".csv"
    Consumers = pd.read_csv(ConsumersFile)
    del ConsumersFile

    del fileID
    
    return Consumers

def readParamFile(fileID = "20F"):
    
    ParamsFile = "Firms." + fileID + ".batch_param_map.csv"
    Params = pd.read_csv(ParamsFile)
    del ParamsFile
    
    del fileID
    
    return Params