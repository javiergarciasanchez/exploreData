'''
Created on 14 feb. 2019

@author: javie
'''
import numpy as np
from scipy.optimize import minimize_scalar, minimize
from math import floor

Gini = 0.7
Lambda = (1 + Gini) / (2 * Gini)
Population = 2000
thetaMin = 0.1
cParam = 0.01
gamma = 2
delta = 0.5
z = 0
discountQ = 0.9999
probRichest = 0.99

MinExpDemand = 10

hiP = 300

def minPrice(realQ):
    return max(perceived(realQ) ** delta * thetaMin, cost(realQ))

def maxPrice(realQ):
    return maxLim() * perceived(realQ) ** delta

def expDemand(p, percQ):
    return Population * (thetaMin / loLim(p, percQ)) ** Lambda

def maxLim():
    return thetaMin / (1-(1-probRichest)**(1/Population))**(1/Lambda)

def loLim(p, percQ):
    return max(p / percQ ** delta, thetaMin)

def perceived(realQ):
    return realQ * discountQ

def cost(realQ):
    return cParam * realQ ** gamma

def profit(p, realQ):
    return(p - cost(realQ)) * expDemand(p, perceived(realQ))

def negProfit(x):
    return -profit(x[0], x[1])

def verifyMaxPrice(x):
    return maxPrice(x[1]) - x[0]

def maxProfit():
    res = minimize(negProfit,
                       x0 = (1 , 1),                       
                       constraints = {"type":"ineq", "fun": verifyMaxPrice},
                       options=dict(maxiter=100))
    
    return res.x