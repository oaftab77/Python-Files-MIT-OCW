# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 19:19:41 2018

@author: aftab
"""

import string


def recursion(string, shift):
    dict_final = {}
    n = 0
    
    if shift == 1:
        for char in string:
            dict_final[char] = string[(n + 1) % 26]
            n += 1
        return dict_final
    else:
        temp = recursion(string, (shift - 1) % 26)
        
        for var in temp:
            None
        key_prev = var
        print(temp)
        for key, value in temp.items():
            dict_final[key_prev] = value
            print(key_prev, value)
            key_prev = key
        return dict_final

b = string.ascii_lowercase
a = recursion(b, 26)
print(a)

