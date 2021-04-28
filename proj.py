import pandas as pd
#imports panda library that allows us to load and use the data that we have
pd.set_option('display.max_columns', None)
#optional
data = pd.read_csv('D:/Python workshop/WS 280421/ml-latest-small/ratings.csv')
#puts the ratings file in a variable
movies = pd.read_csv('D:/Python workshop/WS 280421/ml-latest-small/movies.csv')
#puts movie titles and genres in a variable
data = data.merge(movies,on='movieId', how='left')
#merges the movie titles and ratings
Average_rating = pd.DataFrame(data.groupby('title')['rating'].mean())
#puts the average rating of each movie in a variable
Average_rating['Total Ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())
#shows the number of rates of the movies
movie_user = data.pivot_table(index='userId',columns='title',values='rating')
#creates a table where the rows are userIds and the columns represent the movies
correlations = movie_user.corrwith(movie_user['Inception (2010)'])
#uses the corrwith method of the Pandas Dataframe.
#The method computes the pairwise correlation between rows or columns of a DataFrame with rows or columns of Series or DataFrame
recommendation = pd.DataFrame(correlations,columns=['Correlation'])
#loads data into a DataFrame object:
recommendation.dropna(inplace=True)
#The dropna() function is used to remove missing values(removes all the empty values)
recommendation = recommendation.join(Average_rating['Total Ratings'])
#merges the total ratings to the correlation table
recc = recommendation[recommendation['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()
#filters all the movies with a correlation value to the movie and with at least 100 ratings.
recc = recc.merge(movies,on='title', how='left')
#merge the movies dataset for verifying the recommendations.
print(recc.head(10))