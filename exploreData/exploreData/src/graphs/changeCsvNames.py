'''
Created on 13 feb. 2019

@author: javie
'''

import os
os.chdir("C:/Users/javie/OneDrive - AUSTRAL/Investigación - JGS/Sudden Stop - Phoenix Miracle II - PHX (2)/Model/Python/Data")

timeStamp = "2019.feb..13.17_11_44"
newID = "30F"

for filename in os.listdir("."):
    newFN = filename.replace(timeStamp, newID)
    os.rename(filename, newFN)