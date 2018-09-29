# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

########
# Prompt
#Finger exercise: Write a program that asks the user to input 10 integers, and
#then prints the largest odd number that was entered. If no odd number was
#entered, it should print a message to that effect.
########

#Take-aways
#Really think about how you define variables inside and outside of loops

#POTENTIAL IMPROVEMENT: MAKE MAX ODD VALUE NONE!!!

#code from internet
#maxOdd = None
#for _ in range(10):
#    value = int(input('Enter a value: '))
#    if (value % 2 and (maxOdd is None or value > maxOdd)):
#        maxOdd = value
#if maxOdd:
#    print('The largest odd value entered was', maxOdd)
#else:
#    print('No odd values were entered.')
#Note that the above works because 1 is the same as True in boolean and 0 is false

i = 0
highest_odd = 0
userinput = 0
previnput = 0
counter = 1
#A counter will be used to print the error message in case 10 evens are given

print("When prompted, please input the 10 numbers, one after the other: ")

userinput = int(input("Enter first number: "))

if userinput%2 == 1:
    highest_odd = userinput
    while(i != 9):
        previnput = userinput
        userinput = int(input("Enter the number: "))        
        if userinput%2 == 1:
            if userinput > previnput:
                #Issue: if your list has 2, then -1
                #Solution: expand if loop to include an and statement
                highest_odd = userinput
            else:
                highest_odd
        else:
            highest_odd
        i += 1
    print(highest_odd)

else:
    while(i != 9):
        previnput = userinput
        userinput = int(input("Enter the number: "))
        
        if userinput%2 == 1:
            if userinput > previnput:
                highest_odd = userinput
            else:
                highest_odd
        else:
            counter += 1
        i += 1
    
    if counter == 10:
        print("No odd numbers were entered.")
    else:
        print(highest_odd)
