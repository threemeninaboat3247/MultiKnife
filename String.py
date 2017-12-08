# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:53:36 2017

@author: Jackson
"""
'''
string operation
'''

def check_and_get(name,mydict):
    '''
        Check the keys of 'mydict' and return an appropriate, suffixed if needed, string near 'name'.
    '''
    keys=mydict.keys()
    suffix=0
    answer=name
    while True:
        if not answer in keys:
            return answer
        else:
            answer=name+str(suffix)
            suffix=suffix+1