# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 13:31:38 2021

@author: gokul
"""

def kadanesAlgorithm(array):
    """
    Takes in a non-empty input array and return max of sum that 
    can be achieve by adding a sub array containing adjacent elements
    """
    sub_array = [array[0]]
    max_till_now = array[0]
    max_of_all = array[0]
    for i in range(1, len(array)):
        if array[i] > max_till_now + array[i]:
            sub_array = [array[i]]
        elif array[i] < (max_till_now + array[i]) and array[i]>=0:
            sub_array.append(array[i])
        #print(array[i], max_till_now + array[i])
        max_till_now = max(array[i], max_till_now + array[i])
        max_of_all = max(max_of_all, max_till_now)
    
    print(sub_array)
    return max_of_all

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

kadanesAlgorithm(array)