'''
Created on 13 feb. 2019

@author: javie
'''


# Rename Files
def renameFiles(oldN, newN):
    import os
#    os.chdir("C:/Users/javie/OneDrive - AUSTRAL/Investigación - JGS/Sudden Stop - Phoenix Miracle II - PHX (2)/Model/Python/Data")

    for filename in os.listdir("."):
        newFN = filename.replace(oldN, newN)
        os.rename(filename, newFN)
        
    return

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

def readDataFiles(fileID = "20F"):

#    import os
#    path = "C:\\Users\javie\OneDrive - AUSTRAL\\Investigación - JGS\\Sudden Stop - Phoenix Miracle II - PHX (2)\\Model\\Python\\Data"    
#    os.chdir(path)
    
    Firms = readFirmFile(fileID)
    Consumers = readConsumerFile(fileID)
    Params = readParamFile(fileID)
    
    return [Firms, Consumers, Params]
