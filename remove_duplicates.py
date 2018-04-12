import pandas
import numpy as np

ratings_data = pandas.read_csv("bgg_ratings.csv", sep='\t', dtype={"game_id": "category", "game_name": "category", "username": "category"})
ratings_data.drop(['rating_num'], axis = 1)

print(ratings_data.head())
print(ratings_data["rating"].describe())

print("Row count: ", ratings_data.shape[0])

# remove duplicate records
ratings_data.drop_duplicates(inplace = True)

print("Row count: ", ratings_data.shape[0])

ratings_data.to_csv("bgg_ratings_clean.csv", sep = '\t', index = False)

