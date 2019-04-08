import pandas as pd

df = pd.read_csv('ratings_small.csv')
df_grouped = df.groupby('movieId')

dict_list = []

# iterate over all entries in the GroupBy Object, determine mean and median for each movie and create a dictionary
# for each entry in this format: {'id': 1, 'rating_mean': 3.8724696356275303, 'rating_median': 4.0}
for _id, group in df_grouped:
    row = {
        'movieId': _id,
        'mean': group['rating'].mean(),
        'median': group['rating'].median()
        }
    dict_list.append(row)
    
    
for row in dict_list:
    print(row)
