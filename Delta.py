# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:16:56 2017

@author: Press150
"""
import logging

def set_2182A(gpib=8,nplc=10,settling_time=0.5):
    '''
    Set the sourcemeter for Delta measurement
    
    Parameters:
        gpib: int
            the gpib address of the nanovoltmeter
        nplc: int
            the number of cycles in AC/DC convert
        settling_time: float
            time interval(/sec) between voltage measurement and current change
    '''
    
    import visa
    rm=visa.ResourceManager()
    n=rm.get_instrument('GPIB::{}'.format(gpib))
    
    n.write(":syst:pres")
    n.write('sens:volt:nplc {}'.format(nplc))
    n.write(":sens:volt:delt on")
    n.write(":trig:sour ext")
    n.write(':trig:delay {}'.format(settling_time))
    logging.info('successfully set Delta mode for 2182A')
    
def set_2401(sweep_points,gpib=24):
    '''
    Set the sourcemeter for Delta measurement
    
    Parameters:
        gpib: int
            the gpib address of the sourcemeter
        sweep_points: list
            sweep current points
    '''
    
    import visa
    rm=visa.ResourceManager()
    s=rm.get_instrument('GPIB::{}'.format(gpib))  
    
    #configure the trigger model
    s.write('*RST')
    s.write(':arm:sour immediate')
    s.write(':arm:OLINE 3')
    s.write(':arm:count infinite')
    
    s.write(':TRIGger:SOURce TLINK')
    s.write(':TRIGger:ILINE 1')
    s.write(':TRIGger:INPut SOURce')
    
    s.write(':TRIGger:OLINe 2')
    s.write(':TRIGger:OUTPut SOURce')
    s.write(':TRIGger:DEL 0')
    s.write(':TRIGger:COUNt {}'.format(len(sweep_points)))
    
    #set up the sourcemeter to source current and meaure voltage
    s.write(':sour:func curr;')
    s.write(':func \'volt\';')
    
    #set the sweep points
    string=(('{},'*len(sweep_points)).format(*sweep_points)).strip(',')
    s.write(':sour:list:current '+string)
    logging.info('successfully set Delta mode for 2401')
    
#n.write(':trace:clear')
#n.write(':TRACE:FEED:CONT NEXT')
#n.write(':TRACE:POINTS 6')
#n.write(':TRACE:FEED SENSE')