import numpy

import pandas as pd


def to_float(x): 
    try: 
        x = float(x) 
    except: 
        x = numpy.nan 
    return x 
    
def add_column(df):
    #von der Angabe
    small_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()
    small_df.loc['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce')
    small_df['release_year'] = small_df['release_date'].apply\
        (lambda x: str(x).split('-')[0] if x != numpy.nan else numpy.nan)
    small_df['release_year'] = small_df['release_year'].apply(to_float)
    small_df['release_year'] = small_df['release_year'].astype('float')
    small_df = small_df.drop(columns="release_date")
    return small_df


df = pd.read_csv('movies_metadata.csv', encoding='utf-8', low_memory=False)
print(type(df))

#show information about first movie
print(df[:1].to_string())

#show information about Jumanji
print(df.loc[df['title'] == 'Jumanji'].to_string())

#create a smaller version with fewer columns
s_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']]
#print(s_df)

#add realease year to the data frame
small_df = add_column(s_df)
#print(small_df)

#print the titles of all movies that were released after 2010
print(small_df.loc[small_df['release_year'] > 2010].to_string())
        
    



