#!/usr/local/bin/python3

import collections
from pprint import pprint
#import multiprocessing
#from multiprocessing import Pool, Process, freeze_support
import concurrent.futures
import time

##---------------------------------
def print_timing(function_name, start_time):
    timeEnd = time.time()
    print("---", function_name, " took  ",  round((timeEnd-start_time), 1), " seconds", "\n\n" )
    print('')
    
##---------------------------------
Scientist = collections.namedtuple('Scientist', [
    'name',
    'born',
])

scientists = (
    Scientist(name='Ada Lovelace', born=1815),
    Scientist(name='Emmy Noether', born=1882),
    Scientist(name='Marie Curie', born=1867),
    Scientist(name='Tu Youyou', born=1930),
    Scientist(name='Ada Yonath', born=1939),
    Scientist(name='Vera Rubin', born=1928),
    Scientist(name='Sally Ride', born=1951),
)

pprint(scientists)
print()

 ##---------------------------------
def transform(x):
    time.sleep(1)
    return {'name': x.name, 'age': 2017-x.born}
    
#------------------------
start = time.time()
result = tuple(map(transform, scientists))
pprint(result)
print_timing('ordinary map: ', start)

#------------------------
start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(transform, scientists)
        
pprint(tuple(result))
print_timing('futures map: ', start)
