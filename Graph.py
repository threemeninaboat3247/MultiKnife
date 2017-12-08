# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:13:32 2017

@author: Jackson
"""

def applyCalibTemplate(ax):
    '''
    Apply the template for calibrations to the ax
    Parameters:
        ax: matplotlib.axes._subplots.AxesSubplot
            the ax to which the template is applied
    '''
    import matplotlib
    matplotlib.rcParams.update({'font.size': 18})
    ax.tick_params(axis='both',which='both',labelsize='14')
    ax.grid(which='both',axis='both')
    
    fig=ax.get_figure()
    fig.canvas.draw()
    
def applyThesisTemplate(ax,marker='o',markersize=4):
    '''Apply the template for figures in a thesis to the ax
    Parameters:
        ax: matplotlib.axes._subplots.AxesSubplot
            the ax to which the template is applied
    '''
    import matplotlib
    matplotlib.rcParams.update({'font.size': 14})
    
    import matplotlib.cm as cm
    lines=ax.get_lines()
    
    delta=0
    num=len(lines)
    if num>1:
        delta=1/(num-1)
    
    for index,line in enumerate(lines):
        line.set_linestyle('None')
        line.set_marker(marker)
        line.set_markeredgewidth(0)
        line.set_markersize(markersize)
        line.set_markerfacecolor(cm.hsv(index*delta))
    
    fig=ax.get_figure()
    fig.canvas.draw()    