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
dict2 = random_dict(6000)
#print('dict2: ', dict2, '\n\n')
dict_items = dict2.items()

def convert_list_of_tuples_into_simple_list(input_list):
    return [item for t in input_list for item in t]

def convert_simple_list_to_dict(simp_list): 
#    print('simp_list: ', simp_list)
    it = iter(simp_list) 
    res_dct = dict(zip(it, it))
    return res_dct 
      
start = time.time()   
result_list = list( map(transform, dict_items))
simple_list = convert_list_of_tuples_into_simple_list(result_list)
result_dict = convert_simple_list_to_dict(simple_list)
print_timing('6000 items() in; dict out ',start)
    
def main():
   with ThreadPoolExecutor(max_workers = 4) as executor:
      start = time.time()   
      results = list(executor.map(transform, dict_items))
      simple_list = convert_list_of_tuples_into_simple_list(results)
      result_dict = convert_simple_list_to_dict(simple_list)
      print_timing('6000 ThreadPoolExecutor ',start)

if __name__ == '__main__':
   main()
