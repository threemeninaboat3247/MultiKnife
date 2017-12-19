# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:13:32 2017

@author: Jackson
"""

def graph_set(g,xlabel,ylabel,title=None):
    '''
    input
        g: jh.GraphWindow
        ---
    output
        None
    description
        jh.GraphWindowにテンプレートを適用する
    '''
    import matplotlib.ticker as ptick ##これが必要！
    
    ax=g.fig.get_axes()[0]
    if not title==None:
        ax.set_title(title,fontdict={'fontsize':24})
    ax.set_xlabel(xlabel,fontdict={'fontsize':20})
    ax.set_ylabel(ylabel,fontdict={'fontsize':20})
    ax.tick_params(labelsize=20)

    ax.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True)) 
    ax.yaxis.offsetText.set_fontsize(20)
    ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    
def matplot_color_grad(parent,x,y,xlabel,ylabel,markersize=4):
    '''
    Description:
        Plot data in the child folders of the parent folder
    Parameters:
        parent: parent folder
        x/y: the name of x/y data
        x/ylabel: the label of x/y axis
    Return:
        jh.GraphWindow
    '''
    import jupyterhack as jh
    import matplotlib.cm as cm
    
    children=[cur for cur in parent.getChildren().values() if isinstance(cur,jh.MyTree.MyTree)]
    s_children=sorted(children,key=lambda x: x.name)
    g=jh.GraphWindow()
    length=len(s_children)
    for index,child in enumerate(s_children):
        label=child.name.split('_')[1]
        color=cm.hsv(index/length)
        g.plot(child.get(x),child.get(y),label=label,color=color,
               marker='o',ls='None',mew=0,markersize=markersize)
    ax=g.fig.get_axes()[0]
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    return g

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