"""
Nog's Population Calculator v.1.0
Population Calculating Module

Arguments:
Current Population
Population Growth Rate
"""
import random

def NPSPopcalc(popCurrent, growthRate):
    random.seed(a=None, version=2)
    growthVariance = random.randint(-10, 10) * 0.01
    growthRate = growthRate * growthVariance
    growthMultiplier = growthRate * 0.01 + 1
    popNew = popCurrent * growthMultiplier
    return popNew
