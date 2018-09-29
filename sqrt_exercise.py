# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 23:30:01 2018

@author: aftab
"""
####################
## EXAMPLE: perfect squares
####################

####################
## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
####################


ans = 0
neg_flag = False
numofiterations = 0

x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < abs(x):
    ans += 1
    numofiterations +=1
    
if ans**2 == abs(x) and neg_flag == False:
    print("Square root of", x, "is", ans)
elif ans**2 == abs(x) and neg_flag == True:
    print("Imaginary square root of " + str(x) + " is +/- " + str(ans) + "i")
else:
    print(x, "is not a perfect square")
print("Number of iterations is", numofiterations)
