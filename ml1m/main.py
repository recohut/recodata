import pandas as pd

ratings = pd.read_csv('ml1m/ratings.dat',
                      header=None,
                      sep='::',
                      engine='python',
                      names=['user_id', 'movie_id', 'rating', 'timestamp'])

users = pd.read_csv('ml1m/users.dat', 
                    sep='::', 
                    engine='python', 
                    encoding='latin-1',
                    names=['userid', 'gender', 'age', 'occupation', 'zipcode'])

movies = pd.read_csv('ml1m/users.dat', 
                    sep='::', 
                    engine='python', 
                    encoding='latin-1',
                    names=['movieid', 'title', 'genre'])