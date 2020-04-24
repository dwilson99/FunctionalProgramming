#!/usr/local/bin/python3

import time
import multiprocessing
from multiprocessing import Pool, Process, freeze_support

if __name__ == '__main__':
    freeze_support()

##----------------------------------
def print_timing(function_name, start_time):
    timeEnd = time.time()
    print("------", function_name, " took  ",  round((timeEnd-start_time), 6), " seconds" )

# function to square a given number

##----------------------------------
listt = [0, -1, 3, 4.5, 99, .08]
max = int(1e5)
tuple_1 = range(max)
tuple_2 = tuple(tuple_1)

# using 'map' to call the function #
##----------------------------------
def squareNum(j):
    sum = 0
    x = j * j
    sum = sum + x
print('sum inside def', sum)
    
#print(" squareNum(max):", squareNum(max))
#     'squareNum' for all the elements # of 'listt'
##----------------------------------
start = time.time() 
result = 0
answer = list(map(squareNum, tuple_2))
print_timing("map", start) 
     # map function returns an iterator
a2 = answer[len(answer)-2]
print('map result', a2)
     # convert map to list
#print(list(x))
     # alternate way to square all
     # elements of 'listt' using
     # 'for loop'
##----------------------------------
start = time.time() 
result = 0
for i in tuple_1 : 
    square = i * i
    result = result + square
print_timing("for  loop", start) 
print('loop result', result)

##----------------------------------
''''
pool = multiprocessing.Pool()

start = time.time()
result = 0
answer = list(pool.map(squareNum, tuple_2))
print_timing("multiprocessing", start)
a2 = answer[len(answer)-1]
print('multiprocessing map result', a2)
'''

