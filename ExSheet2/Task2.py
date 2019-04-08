
import pandas as pd
 
data = [['Toy Story', 21.946943],
        ['Jumanji', 17.015539],
        ['Grumpier Old Men', 11.7129]]     

df = pd.DataFrame(data, columns=['title', 'popularity'])

#create sortet data frame
sorted_df =  df.sort_index()

print(sorted_df['popularity'])