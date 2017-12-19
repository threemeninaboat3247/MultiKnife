# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:51:23 2017

@author: Press150
"""

def voltage2pressure(x):
    '''BiとTeの構造相転移点から決定した校正曲線　ポンプセンサーの電圧値(V)に対して圧力(GPa)を返す　有効な定義域：[0,2] (V)'''
    params=[ -1.93092740e+00,   8.37959568e+00,   9.99929962e-05]
    def quadratic(params,x):
        return params[0]*x**2+params[1]*x+params[2]
    return quadratic(params,x)
    
def ton2voltage(x):
    '''圧力コントローラの表示値(ton)に対してポンプセンサーの電圧値(V)を返す'''
    v=0.014579*x+0.013609
    return v
    
def ton2pressure(x):
    '''圧力コントローラの表示値(ton)に対して圧力(GPa)を返す'''
    p=voltage2pressure(ton2voltage(x))
    return p
    
def voltage2ton(x):
    '''ポンプセンサーの電圧値(V)に対して圧力コントローラの表示値(ton)を返す'''
    t=(x-0.013609)/0.014579
    return t