
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:37:50 2018

@author: aftab
"""
####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################

i = 0

n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right":
    if i < 2 and n == "right":
        i += 1
        n = input("You are in the Lost Forest\n****************\n****************\n :(\n****************\n****************\nGo left or right? ")     
    elif n == "right":
        n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")

# =============================================================================
# Take-away
# for loop was inappropriate for this because it always executed inside the while loop
# It was necessary to program a contingency for the situation where it's one right and then left, hence the if _ and _
# 
# =============================================================================
