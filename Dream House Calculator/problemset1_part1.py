# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 20:37:27 2018

@author: aftab
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
down_payment = 0.25*total_cost
current_savings = 0.0
r = 0.04
months = 0
while current_savings <= down_payment:
    current_savings = current_savings + (portion_saved*annual_salary/12) + (current_savings*r/12)
    months += 1
print("Number of months", months)
