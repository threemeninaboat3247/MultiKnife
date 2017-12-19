# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:56:24 2017

@author: Press150
"""
import visa,re

def pick_gpib():
    '''show connected gpib instruments'''
    rm=visa.ResourceManager()
    insts=rm.list_resources()
    for x in insts:
        standard=x.split('::')[0]
        if standard=='GPIB0':
            inst=rm.get_instrument(x)
            info=inst.query('*IDN?')
            num=x.split('::')[1]
            print('GPIB '+num+' :: '+info)
            
def set_delta(sour_add=24,nano_add=8):
    '''set Delta mode of 2401 and 2182A'''
    sour=GpibInst(sour_add)
    nano=GpibInst(nano_add)
    
    nano.write(":syst:pres")
    nano.write(":sens:volt:delt on")
    nano.write(":trig:sour ext")
    
    sour.write(':sour:func curr;')
    sour.write(':func \'volt\';')
    sour.write(':OUTP ON')
    
    #sweep configure
    sour.write(':sour:list:current -0.001,0.001')
    sour.write(':arm:sour IMM')
    sour.write(':arm:OLINE 3')
    sour.write(':arm:OUTPut NONE')
    sour.write(':arm:COUNt INFINITE')
    sour.write(':TRIGger:SOURce TLINK')
    sour.write(':TRIGger:ILINE 1')
    sour.write(':TRIGger:INPut SOURce')
    sour.write(':TRIGger:OLINe 2')
    sour.write(':TRIGger:OUTPut SOURce')
    sour.write(':TRIGger:DEL 0')
    sour.write(':TRIGger:COUNt 2')
    
    print('Please push \'SWEEP\' button of 2401 and set \'TYPE\' to \'CUSTOM\' and \'SWEEP-COUNT\' to \'INFINITE\'.')
    print('Then back to the start state and push \'SWEEP\' and \'TRIG\'. The measurement will start.')        

    
class GpibInst():
    pattern=re.compile(r'^[\+-]?\d*\.?\d*E[\+-]?\d*')
    def __init__(self,gpib):
        rm=visa.ResourceManager()
        self.inst = rm.get_instrument("GPIB::"+ str(int(gpib)))
        
    def query(self,command,raw_string=False):
        answer=self.inst.query(command)
        if raw_string:
            return answer
        else:
            body=self.pattern.match(answer).group()
            return float(body)
    
    def write(self,command):
        self.inst.write(command)
        return True