# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 00:24:05 2018

@author: aftab
"""
    
highestodd = None
i = 0

while (i != 10):
    inp = int(input("Enter a number: "))
    if(inp %2 and (highestodd is None or inp > highestodd)):
        highestodd = inp
    i +=1
if highestodd:
    print("Highest odd: {}".format(highestodd))
else:
    print("No odds entered")

