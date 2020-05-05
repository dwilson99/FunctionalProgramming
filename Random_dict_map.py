#!/usr/local/bin/python3

from collections import Counter
import json
import math
import collections
import time
#import concurrent.futures
from pprint import pprint
from time import sleep
from timeit import timeit
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed

##---------------------------------
def print_timing(function_name, start_time):
    timeEnd = time.time()
    print(function_name, " took  ",  round((timeEnd-start_time), 1), " seconds", "--------" )

#------------------------
def random_dict(n):
    from random import randrange, randint
    mydict = {'key'+str(i):i for i in range(n)}
    sleep(0.1)
#    mydict['key'+str(randint(0,n-1))] = 'value2'
    return mydict

#------------------------

def transform(item):
#    print('item: ', item)
    y = list(item)
    y[1] = y[1] + 500
    item = tuple(y)
#    print('item: ', item)
    sleep(0.01)
    return item

#------------------------
NUMBER_ITEMS = 500
  
dict2 = random_dict(NUMBER_ITEMS)
if (NUMBER_ITEMS <8):
    print('dict2: \t\t', dict2, '\n\n')
dict_items = dict2.items()

def convert_list_of_tuples_into_simple_list(input_list):
    return [item for t in input_list for item in t]

def convert_simple_list_to_dict(simp_list): 
#    print('simp_list: ', simp_list)
    it = iter(simp_list) 
    res_dct = dict(zip(it, it))
    return res_dct 

def convert_list_of_tuples_into_dict(input_tuple):
    return [item for t in input_list for item in t]

def convert_list_to_dict(a_list): 
    simple_list_local = convert_list_of_tuples_into_simple_list(a_list)
    dct = convert_simple_list_to_dict(simple_list_local)
    return dct 
    
def test_map():
    start = time.time()   
    result_list = list( map(transform, dict_items))
    simple_list = convert_list_of_tuples_into_simple_list(result_list)
    result_dict = convert_simple_list_to_dict(simple_list)
    dct2 = convert_list_to_dict(result_list)
    if NUMBER_ITEMS < 8:
        print('result_dict: \t', result_dict)
    timing_name = str(NUMBER_ITEMS) + ' items() in; dict out '
    print_timing(timing_name,start)

def test_Thread_pool_map():
   with ThreadPoolExecutor(max_workers = 4) as executor:
       start = time.time()   
       results_list = list(executor.map(transform, dict_items))
       result_dict = convert_list_to_dict(results_list)
       timing_name2 = '\n' + str(NUMBER_ITEMS) + ' ThreadPoolExecutor '
       print_timing(timing_name2,start)
       
def main():
    test_map()
    test_Thread_pool_map()

if __name__ == '__main__':
    main()
