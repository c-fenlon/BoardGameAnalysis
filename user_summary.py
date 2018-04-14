user_pivot = pandas.pivot_table(ratings_data, values = 'rating', index = ['username'], aggfunc = (len, np.mean))
user_pivot.sort_values(by = ('len'), ascending = False, inplace = True)
print(user_pivot)

print("Mean number of reviews:", np.mean(user_pivot.len))
print("Median number of reviews:", np.median(user_pivot.len))
