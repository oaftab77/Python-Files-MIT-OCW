# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 15:38:09 2018

@author: aftab
"""
def timedownpayment(annual_salary, portion_saved, total_cost):
    """
    Assumes that user enter annual_salary, portion_saved per year, and total_cost as floats
    Returns months needed to save for a down payment assuming downpayment is 25% of TC and r = 0.04, compounded monthly
    """
# =============================================================================
#     annual_salary = float(input("Enter your annual salary: "))
#     portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
#     total_cost = float(input("Enter the cost of your dream home: "))
# =============================================================================
    down_payment = 0.25*total_cost
    current_savings = 0.0
    r = 0.04
    months = 0
    while current_savings <= down_payment:
        current_savings = current_savings + (portion_saved*annual_salary/12) + (current_savings*r/12)
        months += 1
    print("Number of months", int(months))
    return months

def test_timedownpayment():
    """
    Assumes user enters a list of numbers IN THE FORMAT Annual_Salary,Portion_Saved,Total_Cost
    Tests entered numbers to see if expected values are produced
    """
    #list_of_tests = (120000, 0.1, 1000000, 80000, 0.15, 500000)
    #From problem set 1
    
    list_of_tests = ()
    listofnum = input("Enter the list of num with no spaces ")
    
    for n in listofnum.split(","):
        n = float(n)
        list_of_tests = list_of_tests + (n,)
    
    for counter in list_of_tests:        
        i = list_of_tests.index(counter)
        if i%3 == 0:
            annual_salary = counter
        elif i%3 == 1:
            portion_saved = counter
        else:
            total_cost = counter
            print(annual_salary, portion_saved, total_cost)
            months = timedownpayment(annual_salary, portion_saved, total_cost)
            print(months)

test_timedownpayment()        