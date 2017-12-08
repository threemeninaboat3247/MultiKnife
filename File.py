# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:09:57 2017

@author: Yuki
"""
'''
File Operation
'''

import os

def find_all_files(directory):
    '''
    Return all the files under a directory
    
    Parameters:
        directory: str
            the absolute path of the directory to search
    Returns:
        list
            the absolute pathes of files
    '''
    
    def mygenerator(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                yield os.path.join(root, file)
    
    return list(mygenerator(directory))
