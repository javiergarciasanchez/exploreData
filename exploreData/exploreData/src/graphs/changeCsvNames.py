'''
Created on 13 feb. 2019

@author: javie
'''

import os
os.chdir("C:/Users/javie/OneDrive - AUSTRAL/Investigación - JGS/Sudden Stop - Phoenix Miracle II - PHX (2)/Model/Python/Data")

os.listdir(".")

timeStamp = "2019.feb..22.11_00_12"
newID = "1F"

for filename in os.listdir("."):
    newFN = filename.replace(timeStamp, newID)
    os.rename(filename, newFN)