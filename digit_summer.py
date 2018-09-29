# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:21:25 2018

@author: aftab
"""
def splitterwithdelim(string, delimeter):
    """
    Splits string on delimeter like "."
    Very literal in interpretation, "0.1233.123" becomes ["0.1233", ".123"] not ["0.123", "3.123"]
    Commas inbetween won't solve as this splices strings
    """
    index = 0
    firstchar = 0
    s = []
    if "." in string:
        for i in range(string.count(delimeter) + 1):            
            index = string.find(delimeter, index + 1)
            print(index)
            
            if index != -1:
                s.append(string[firstchar:index])
            else:
                s.append(string[firstchar:])
            
            firstchar = index
            if firstchar == 0:
                firstchar = 1
            print(s)
    return s

def sumDigits(s):
    """ 
    Assumes s is a string
    Returns sum of decimal digits (numbers) in s
    ie if input is "abc23" returns 5
    Decimals are summed based on how splitterwith delim splits the string
    Very literal in interpretation, "0.1233.123" becomes ["0.1233", ".123"] not ["0.123", "3.123"]
    """
    sum = 0
    n = 0
    i = 0
    
    if "." in s:
        s = splitterwithdelim(s, ".")
    print(s[i])
    
    for char in s:
        try:            
            char = float(char)
            sum += char
        except ValueError:
            n += 1
        i += 1
    print("The total sum is:", sum, end = ". ")
    if n > 0:
        print("However,", n, "non-int character(s) were detected.")
    return sum

#s = sumDigits("3.001,2.003")

s = sumDigits("3.0012.003")