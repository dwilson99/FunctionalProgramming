#!/usr/local/bin/python3

import time
import multiprocessing
from multiprocessing import Pool, Process, freeze_support

### ------------------
def print_timing(function_name, start_time):
    timeEnd = time.time()
    print("------", function_name, " took  ",  round((timeEnd-start_time), 6), " seconds", "\n\n" )
    print('')

## ------------------
tup = range(1, 11)
print(tup)
listt = [0, -1, 3, 4.5, 99, .08] 
limit = 5000000

# function to square a given number 
## ------------------
def squareNum (a) : 
    return a * a 
 
### ------------------
def old(tup):
    for x in range(limit):
        for i in tup : 
            square = i * i 
    print("old(): ", square) 
  
##----------------------------------
start = time.time() 
old(tup)
print_timing("old", start) 
start = time.time() 
  
  
# using 'map' to call the function 
# 'squareNum' for all the elements 
# of 'listt'
##----------------------------------
start = time.time() 
x = map(old, listt) 
print(list(x))  
print_timing("map", start) 
# map function returns a map 
# object at this particular  
# location 
print(x)  
  
# convert map to list 
  
  
# alternate way to square all 
# elements of 'listt' using 
# 'for loop' 

##----------------------------------
pool = multiprocessing.Pool()

start = time.time()
result = pool.map(old, listt)
print(result)
print_timing("multiprocessing", start)
