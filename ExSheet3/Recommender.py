
import pandas as pd
from _overlapped import NULL

# get user id from console
userID = input("Insert UserID: ")
 
# get movie data from csv files
ratings = pd.read_csv('../ml-1m/ratings.dat', sep="\:\:", names=["userId", "movieId", "ratings", "timestamp"], engine='python')
movies = pd.read_csv('../ml-1m/movies.dat', sep="\:\:", names=["movieId", "title", "genres"], engine='python')
 
# all users grouped by user id
user_group = ratings.groupby('userId')
 
# my user 
my_user = user_group.get_group(int(userID))
my_movie_ids = set(my_user['movieId'])
my_movies = movies.loc[movies['movieId'].isin(my_movie_ids)]

# merge user and his movies
my_user_complete = pd.merge(my_user, my_movies, on="movieId")
my_user_complete = my_user_complete.sort_values('ratings', ascending = False)



i = 0
while i < 20 and my_user_complete.iloc[i] != None:
    print(my_user_complete.iloc[i])
    i+=1
    
 
print(my_user_complete)