# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:23:48 2018

@author: aftab
"""
total_cost = 1000000.0
semi_annual_raise = 0.07
annual_return_rate = 0.04
down_payment = 0.25*total_cost
months = 36
salary = float(input("Enter the starting salary: "))
sal_initial = salary

savings_rate = 0.0
low = 0 #percent*100
high = 10000 #percent*100

guess = (low+high)//2
savings_rate_guess = guess/10000

total_savings = 0.0
for months in range(1,37):
    if months % 6 == 0:
        salary = salary*(1+semi_annual_raise)
    total_savings = total_savings + (savings_rate_guess*salary/12) + (total_savings*annual_return_rate/12)

numofiterations = 0

while abs(total_savings - down_payment) >= 100 and savings_rate_guess < 0.9999:
    if total_savings > down_payment:
        high = guess
    else:
        low = guess    
    #Note the following conditional allows for extremely high incomes where the saving rate needed is very small (beyond 4 decimals)
    #Need to adjusg savings_rate_guess to 1.0 if you enable the else statement below
    if abs(high - low) > 1:
        guess = (low + high)//2
# =============================================================================
    #     else:
#         guess = (low + high)/2
# =============================================================================
    savings_rate_guess = guess/10000
    
    total_savings = 0
    salary = sal_initial
    
    for months in range(1,37):
        total_savings = total_savings + (savings_rate_guess*salary/12) + (total_savings*annual_return_rate/12)
        if months % 6 == 0:
            salary = salary*(1+semi_annual_raise)
    numofiterations += 1

if savings_rate_guess >= 0.9999:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate is", savings_rate_guess)
    print("Number of iterations is", numofiterations)