# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 21:54:31 2018

@author: aftab
"""

# =============================================================================
# Finger exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.
# =============================================================================

integer = int(input("Enter a positive or negative integer (or 0): "))
root = 0
pwr = 0
#Say 2 < pwr < 6
#I added the if statement line in because inputting 0 skipped the while loop
if integer == 0:
    pwr = 0 #DELETE
    print("Root is", root, "and power is", pwr +1)
else:
    while root**pwr != abs(integer) and pwr < 6:
        root = 0
        pwr += 1    
        while root**pwr != abs(integer) and root <= abs(integer) + 1:
            root +=1 
    if root**pwr == abs(integer):
        if integer < 0:
            root = -root
        print("Root is", root, "and power is", pwr)
    else:
        print("No such pair of integers exists")
            


# =============================================================================
# #FOLLOWING IS A FOR LOOP I WROTE FOR FUN
# #Provides (ironically) shorter solution to the 0 problem when pwr's range is not 0 < pwr < 6
# integer = int(input("Enter a positive or negative integer (or 0): "))
# for pwr in range(3, 6):
#         root = 0
#         while root**pwr != abs(integer) and root <= abs(integer) +1:
#             root +=1
#             print(root)
#             print(str(pwr) + "hi")
#         if root**pwr == abs(integer):
#             break            
# if root**pwr == abs(integer):
#     if integer < 0:
#         root = -root
#     print("Root is", root, "and power is", pwr)
# else:
#     print("No such pair of integers exists")
# #####PUT BREAK AT THE END OF THE LOOP AFTER ANY NESTED LOOPS!!! TOOK 20 MINUTES TO REALIZE THAT PUTTING IT IN THE BEGINNING DOESN'T BREAK THE CORRECT LOOP        
# 
# =============================================================================
