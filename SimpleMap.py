#!/usr/local/bin/python3

import multiprocessing
from multiprocessing import Pool, Process, freeze_support
import time
import math as m
import sys
import os

##---------------------------------
def print_timing(function_name, start_time):
    timeEnd = time.time()
    print("---", function_name, " took  ",  round((timeEnd-start_time), 6), " seconds", "\n\n" )
    print('')
    
##---------------------------------
r_max = 10000
tup_1 = (0, 3 , 3, 12)
tup_big = range(1, 800)

##---------------------------------
def compute2(a):
    sum = 0
    for i in range(0, r_max):
        x =  m.sin(a)
        sum = sum + x

print('compute 2 result: ', sum)
     
##---------------------------------
start = time.time()
for a in tup_big : 
    sum = 0
    for i in range(0, r_max):
        x =  m.sin(a)
        sum = sum + x
#    print('compute 2 result: ', sum)
print_timing("for loop", start)

    # using 'map' to call the function 
    # 'squareNum' for all the elements 
    # of 'listt' 
##---------------------------------
start = time.time()
x = map(compute2, tup_big) 
# map function returns a map 
# object at this particular  
# location 
print_timing("map", start)
  
    # convert map to list 
     #print(list(x), "\n")  



#print('multiprocessing: ', tuple(result), "\n")


# alternate way to square all 
# elements of 'listt' using 
# 'for loop' 
if __name__ == '__main__':
    freeze_support()
 

