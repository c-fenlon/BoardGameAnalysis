game_pivot = pandas.pivot_table(ratings_data, values = 'rating', index = ['game_name'], aggfunc = (len, np.mean))
game_pivot.sort_values(by = ('len'), ascending = False, inplace = True)
print(game_pivot)

print("Mean number of reviews per game:", np.mean(game_pivot.len))
print("Median number of reviews per game:", np.median(game_pivot.len))
print("Percentiles of reviews per game:", np.percentile(game_pivot.len, [5, 10, 90, 95]))
