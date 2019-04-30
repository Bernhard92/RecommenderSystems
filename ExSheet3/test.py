import pandas as pd


movies = pd.read_csv('../movie_data/movies_metadata.csv', low_memory=False)


print(movies.loc[movies['id'] == ''])
