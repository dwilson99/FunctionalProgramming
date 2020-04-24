#!/usr/local/bin/python3

import collections
from pprint import pprint
import multiprocessing
from multiprocessing import Pool, Process, freeze_support

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

Scientist_2 = collections.namedtuple('Scientist_2', [
    'name',
    'born',
])

pprint(scientists)
print()

def process_item(item):
    return {
        'name': item.name,
        'age': 2017 - item.born
    }
    
def transform(x):
    return {'name': x.name, 'age': 2017-x.born}
    
result = tuple(map(
        transform,
        scientists
))
pprint(result)

'''
pool = multiprocessing.Pool()
result_2 = tuple(pool.map(
    transform, 
    scientists
))
pprint(result_2)

d = dict()
for sc in scientists:
   d.update( transform(sc) )
pprint(d)
'''

if __name__ == '__main__':
    freeze_support()
#r    Process(pool.map).start()
