# new variables
# like/average/dislike - based on https://boardgamegeek.com/wiki/page/ratings classification
def get_rating_category(row):
	if row['rating'] >= 7:
		return 'like'
	elif row['rating'] >= 4:
		return 'average'
	elif row['rating'] < 4:
		return 'dislike'
	else:
		return None
ratings_data['rating_categorical'] = ratings_data.apply(get_rating_category, axis = 1)

print(ratings_data.head())
print(ratings_data['rating_categorical'].describe())

