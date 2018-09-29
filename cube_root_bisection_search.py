# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:39:17 2018

@author: aftab
"""
 


## EXAMPLE: bisection cube root (only positive cubes!)
####################

userinput = float(input("Input the number: "))
epsilon = 0.00001
low = 0.0
high = max(1,abs(userinput))

# =============================================================================
# #replaced by max function
# f abs(userinput) < 1:
#     #test 0
#     low = abs(userinput)
#     high = 1.0
# =============================================================================
guess = (low + high)/2.0

while abs(guess**3 - abs(userinput)) >= epsilon:
    print(guess)
    if guess**3 < abs(userinput):
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0

if userinput < 0:
    guess = -guess
print("The cube root of the number is", guess)
