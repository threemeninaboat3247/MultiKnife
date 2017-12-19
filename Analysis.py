# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:37:28 2017

@author: Yuki
"""

import numpy as np
    
def evaluate_Tc(zeros,target):
    '''
    Description:
        Evaluate Tc by calculating the zero resistivity area from 'zeros'.
    Parameters:
        zeros: zero resistivity points (np.array)
        target:zero resistivity points + finite resistivity points (np.array)
    Return 
        Tc (float)
    '''
    zeros_vol=zeros[:,1]
    mean=np.mean(zeros_vol)
    std=np.std(zeros_vol)
    
    target_vol=target[:,1]
    result=target[np.where(target_vol<mean+std)[0],:]
    index=np.argmax(result[:,0])
    answer=result[index,:]
    return {'T_c':answer[0],'coordinate':answer}

def evaluate_Tc_onset(consts,target):
    '''
    Evaluate Tc_onset by calculating the constant slope area from 'consts'
    
    Parameters:
        consts: np.array2D
            constant slope points
        target: np.array2D
            constant slope points + points in transition
    
    Returns:
        dictionary
            {'Tc_onset': float,'coordinate': np.array2D}
    '''
    
    consts_vol=consts[:,1]
    mean=np.mean(consts_vol)
    std=np.std(consts_vol)
    
    target_vol=target[:,1]
    result=target[np.where(target_vol<mean+std)[0],:]
    index=np.argmin(result[:,0])
    answer=result[index,:]
    return {'Tc_onset':answer[0],'coordinate':answer}