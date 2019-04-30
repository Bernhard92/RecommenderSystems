
import pandas as pd


data = ['Toy Story', 'Jumanji', 'Grumpier Old Men']
        
series = pd.Series(data)
print(series[:1])
print(series[:2])
print(series[-2:])

#insert new indices 
series_i = pd.Series(data, index=['a', 'b', 'c'])
print(series_i['b'])