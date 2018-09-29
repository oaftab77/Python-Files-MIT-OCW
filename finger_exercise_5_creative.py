# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:01:20 2018

@author: aftab
"""

#Finger exercise: Let s be a string that contains a sequence of decimal numbers
#separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
#the sum of the numbers in s.

#Rewrote code in better way
sum = 0.0
userinput = input("Enter number string: ")
index = userinput.index(",")
numberofnum = userinput.count(",") + 1
for i in range(numberofnum):
    number = float(userinput[0:index])
    sum = sum + number
    userinput = userinput[index + 1:]
    if "," in userinput:
        index = userinput.index(",")
print(sum)

# =============================================================================
#First attempt 
#userinput = input("Enter the string of numbers: ")
# 
# numberofdecimals = userinput.count(".")
# index2 = userinput.index(",")
# a = 0.0
# b = index2
# sum = 0.0
# 
# string = userinput[int(a):int(b)]
# 
# for i in range(numberofdecimals):    
#     a = 0.0
#     b = index2    
#     string = userinput[int(a):int(b)]        
#     num = float(string)
#     sum += num    
#     userinput = userinput[int(b)+1:]    
#     if userinput.count(",") != 0:
#         index2 = userinput.index(",")
# 
# print(sum)
# =============================================================================


# Sample Answer at
# https://stackoverflow.com/questions/21212706/python-convert-string-literal-to-float
#s = "1.23,2.4,3.123"
#print s.split(",")        # ['1.23', '2.4', '3.123']
#s = "1.23,2.4,3.123"
#total = sum(map(float, s.split(",")))
#or
#total = sum(float(item) for item in s.split(","))
#or
#total, s = 0, "1.23,2.4,3.123"
#for current_number in s.split(","):
#    total += float(current_number)
