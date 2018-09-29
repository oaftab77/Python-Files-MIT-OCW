# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:30:39 2018

@author: aftab
"""
################
#Prompt:
#Write a program that examines three variables—x, y, and z—
#and prints the largest odd number among them. If none of them are odd, it
#should print a message to that effect.
#Use only if-else statements!
#############

x = int(input("Enter number x:"))
y = int(input("Enter number y:"))
z = int(input("Enter number z:"))

if x%2 == 1:
    if y%2 == 1:
        if z%2 == 1:
            if x > y and y > z:
                print("x is the greatest odd # ({})".format(x))
            elif y > z:
                print("y is the greatest odd # ({})".format(y))
            else:
                print("z is the greatest odd # ({})".format(z))
        else:
            if x > y:
                print("x is the greatest odd # ({})".format(x))
            else:
                print("y is the greatest odd # ({})".format(y))
    else:
        if z%2 == 1:
            if x > z:
                print("x is the greatest odd # ({})".format(x))
            else:
                print("z is the greatest odd # ({})".format(z))
        else:
            print("x is the greatest odd # ({})".format(x))
else:
    if y%2 == 1:
        if z%2 == 1:
            if y > z:
                print("y is the greatest odd # ({})".format(y))
            else:
                print("z is the greatest odd # ({})".format(z))
        else:
            print("y is the greatest odd # ({})".format(y))
    else:
        if z%2 == 1:
            print("z is the greatest odd #({})".format(z))
        else:
            print("No numbers given were odd. This program evaluates the highest of a set of odd numbers")
            
#13 different printed lines because 2^3 = 8 possibilities, and of these 8, there are 5 internal comparisions with odd numbers (OOO, OOE, etc) so 13 total
