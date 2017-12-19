# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:13:32 2017

@author: Jackson
"""
def plot_with_diff(x,y,xlabel='X',ylabel='Y',title='No name'):
    '''Calculate dy/dx and plot a graph in a notebook of Jupyter by using plotly'''
    import plotly
    plotly.offline.init_notebook_mode(connected=False)
    from jupyterhack import MyFunctions
    
    result=MyFunctions.differentiate(x,y)
    x_s=result['sorted_xs']
    y_s=result['sorted_ys']
    diff=result['df']
    data = [
        plotly.graph_objs.Scatter(x=x_s,y=y_s, name=ylabel),
        plotly.graph_objs.Scatter(x=x_s, y=diff, name="diff", yaxis="y2")
    ]
    layout = plotly.graph_objs.Layout(
        title=title,
        xaxis={"title":xlabel},
        yaxis={"title":ylabel},
        yaxis2={"title":'diff', "overlaying":"y", "side":"right"},
    )
    fig = plotly.graph_objs.Figure(data=data, layout=layout)
    plotly.offline.iplot(fig)
    
def matplot(x,y,xlabel='X',ylabel='Y',title='No name'):
    '''Plot a graph by matplotlib.pyplot'''
    import matplotlib.pyplot as plt
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

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
