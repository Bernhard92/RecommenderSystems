
import pandas as pd




# get user id from console
userID = input("Insert UserID: ")
 
# get movie data from csv files
ratings = pd.read_csv('../movie_data/ratings_small.csv')
movies = pd.read_csv('../movie_data/movies_metadata.csv', low_memory=False)
 
# all users grouped by user id
user_group = ratings.groupby('userId')
 
# my user 
my_user = user_group.get_group(int(userID))
my_movie_ids = set(my_user['movieId'])
my_movies = movies.loc[movies['id'].isin(my_movie_ids)]
 
 
 
 
print(my_user)
print('-----------')
print(type(my_movie_ids))
print(my_movie_ids)
print('-----------')
print(my_movies)

