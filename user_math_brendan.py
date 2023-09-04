"""
Name: Brendan Reed
Date: 9/3/2023

Goal:
"highlight your ability write custom functions that call functions in the math module."



"""
import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

#finds area of building (ft^2)
def building_sqft(length, width):
    return length * width

# not sure what kind of function would be used in healthcare analytics, so I'm just going to do finance.
#net income formula
def net_income(revenue, expenses):
    return revenue - expenses

#break-even point = fixed costs (fc) / (sales price per unit (sp) - variable costs per unit (vc))
def break_even(fc, sp, vc):
    return fc / (sp - vc)

#return on investment (roi) 
# roi = [(investment gain (ig) - cost of investment (ci)) / cost of investment (ci)] * 100]
def roi(ig, ci):
    return ((ig - ci) / ci) * 100

#use this one to call a math function
#simple interest = p * r * t
# where p: principal, r: rate of interest, t: time
def simple_interest(p, r, t):
    return math.prod([p,r,t])

logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
logger.info(f"{building_sqft(1500,1000)}")
logger.info(f"{building_sqft(775,980)}")
logger.info(f"{break_even(5000, 25, 8)}")
logger.info(f"{roi(1000,900)}")
logger.info(f"{simple_interest(5000, .07, 10)}")


