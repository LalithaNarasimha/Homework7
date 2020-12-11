#Use random module with a seed of 2020 to generate 20 integers between 100 and 120 (inclusive). Then write code to calculate the median and mode.  The median is the 10th largest number. The mode is the number that occurs the most. If two or more number have the same frequency, list them all.

import random

def calculate_median(p_num_list):
    count = 0

    p_num_list.sort()
    count = len(p_num_list)
    if count%2 == 0:
        median1 = p_num_list[count//2]
        median2 = p_num_list[count//2 - 1]
        median = (median1 + median2)/2
    return median
    

def calculate_mode(p_num_list):
    d_list = {}
    mode_list = []
    high_freq = None

    for num in p_num_list:
        if num in d_list:
            d_list[num] += 1
        else:
            d_list[num] = 1 
 
    #high_freq = max(d_list.values())
    for v in d_list.values():
        if high_freq == None:
            high_freq = v
        if v > high_freq:
            high_freq = v

    for k,v in d_list.items():
        if v == high_freq:
            mode_list.append(k)

    return mode_list
        

#Start of the program
num_list = []
mode_list = []
random.seed(2020)
num_list = [random.randint(100,120) for i in range(20)]
print(f'Random integers between 100 and 120: {num_list} ')
median = calculate_median(num_list)
print(f'Median of the sequence :{median} ')
mode_list = calculate_mode(num_list)
print(f'Modes of the sequence : {mode_list}')