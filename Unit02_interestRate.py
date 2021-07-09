#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:42:31 2021

@author: aghotekar
"""

''' 15% interest rate '''
interest_rate = 1.15

''' initial principal amount '''
money = 1000

''' time of investment in years'''
term = 5

''' money spent after five years '''
lump_sum = 500

''' amonut left after five years '''
after_five_years = (money * (interest_rate ** term)) - lump_sum
print(after_five_years)

''' amount left after ten years '''
after_ten_years = (after_five_years * (interest_rate ** term))
print(after_ten_years)