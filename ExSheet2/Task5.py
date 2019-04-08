import pandas as pd

ratings = pd.read_csv('ratings_small.csv')
movies = pd.read_csv('movies_metadata.csv', low_memory=False)
user_group = ratings.groupby('userId')

# get information of first user in data set
first_user = user_group.get_group(1)

#get movie ids from first user int a set 
firsts_movieIds = set(first_user['movieId'])

#print movies of first user
#print(firsts_movieIds)

relatedUsers = []

#every user that has three or more of the same movies rated, gets added 
#to the list of related users of user1
for user, group in user_group:
    movieIds = set(group['movieId'])
    if(len(firsts_movieIds.intersection(movieIds)) >= 3):
        relatedUsers.append(user)
   
print(relatedUsers)