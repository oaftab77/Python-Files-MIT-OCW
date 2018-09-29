# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:39:01 2018

@author: aftab
"""


# Cube Root Program

i = 0

userinput = float(input("Enter the number: "))
if abs(userinput) < 1:
    string = str(userinput)
    print(string)
    index = string.index(".")
    numofdecimals = len(string[index + 1:])
    counter = "0." + "0"*(numofdecimals+1) + "1"
    #added a +1 for greater accuracy if someone inputs something like 0.2
    counter = float(counter)    
    while i < 1:        
        if i **3 >= abs(userinput):
            break
        i += counter
    if userinput < 0:
        i = -i
    print("The cube root is approximately " + str(i))
else:
    for i in range(0, abs(int(userinput)) +1 ):
        #+1 is there because if you type in 1, it returns no cube root
        if i**3 >= abs(userinput):
            break
    if(i**3 == abs(userinput)):
        if userinput < 0:
            i = -i
        print(i)
    else:
        print("No perfect cube root") 

#Problem: works for 0.1, 0.01, 0.001, 0.0001, but not 0.00001 and onwards? error is with index, it says substring not found
#NOTE: PYTHON STORES DECIMALS LESS THAN 1E-04 IN SCIENTIFIC NOTATION
