# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:59:50 2018

@author: aftab
"""
userinput = float((input("Enter the number: ")))

guess = abs(userinput)/2.0
epsilon = 0.001
numofiterations = 0

while abs(guess**2 - abs(userinput)) >= epsilon:
    guess = guess - (guess**2 - abs(userinput))/(2*guess)
    numofiterations += 1

if userinput < 0:
    guess = -guess
print("The approximate square root is ", guess, "and Number of iterations is", numofiterations)
