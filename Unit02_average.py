#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:14:48 2021

@author: aghotekar
"""

numbers = [13, 5102, 45, 2301.40, 203, 1502, 3]

## Define a variable for sum
numbers_sum = sum(numbers)

#Finish the if-statement
if len(numbers) >= 1:
    average = numbers_sum/len(numbers)
    print(average)
else:
    print(0)