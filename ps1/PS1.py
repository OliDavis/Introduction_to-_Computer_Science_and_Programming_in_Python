# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:41:25 2018

@author: Oliver
"""


#==============================================================================
# #inputs
# annual_salary = int(input("enter annual salary.. "))
# monthly_portion_saved = float(input("enter portion saved (dec).. "))
# cost_of_house = int(input("enter cost of house.. "))
# 
# #constants
# current_savings = 0
# r = 0.04                    #interest rate
# down_payment = 0.25
# month_counter = 0
# 
# #calculations
# monthly_salary = annual_salary/12
# monthly_salary_saved = monthly_salary*monthly_portion_saved
# deposit = cost_of_house*down_payment
# 
# #Calculation Loop
# while current_savings <= deposit:
#     current_savings = (current_savings + monthly_salary_saved)+(current_savings*r/12)
#     month_counter += 1
#     
# print("you will need to save for ", month_counter, "months" )
#==============================================================================

#==============================================================================
 #inputs
annual_salary = int(input("enter annual salary.. "))
monthly_portion_saved = float(input("enter portion saved (dec).. "))
cost_of_house = int(input("enter cost of house.. "))
pay_rise_per = float(input("enter % payrise.. "))
 
#constants
current_savings = 0
r = 0.04                    #interest rate
down_payment = 0.25
month_counter = 0
 
#calculations

 
deposit = cost_of_house*down_payment
 
#Calculation Loop
while current_savings <= deposit:
   if month_counter != 0 and month_counter % 6 == 0:      
       annual_salary += annual_salary*pay_rise_per
    
   monthly_salary = annual_salary/12 
   monthly_salary_saved = monthly_salary*monthly_portion_saved
   current_savings = (current_savings + monthly_salary_saved)+(current_savings*r/12)
   month_counter += 1
     
print("you will need to save for ", month_counter, "months" )
#==============================================================================
