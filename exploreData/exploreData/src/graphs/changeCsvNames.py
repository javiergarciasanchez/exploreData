'''
Created on 13 feb. 2019

@author: javie
'''

import os
os.chdir("C:/Users/javie/OneDrive - AUSTRAL/Investigaci�n - JGS/Sudden Stop - Phoenix Miracle II - PHX (2)/Model/Python/Data")

os.listdir(".")

timeStamp = "2019.feb..23.12_39_18"
newID = "30F"

for filename in os.listdir("."):
    newFN = filename.replace(timeStamp, newID)
    os.rename(filename, newFN)