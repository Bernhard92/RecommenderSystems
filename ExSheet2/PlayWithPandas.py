'''
Created on 8 Apr 2019

@author: Bernhard
'''
import pandas as pd

class PlayWithPandas(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.task1()
        
    def task1(self):
        data = ['Toy Story', 'Jumanji', 'Grumpier Old Men']
        
        series = pd.Series(data)
        print(series[:1])

if __name__ == '__main__':
    pwp = PlayWithPandas()
    
    
    