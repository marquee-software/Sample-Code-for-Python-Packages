import pandas as pd
list_of_dfs = pd.read_html('https://www.ussoccer.com/uswnt-stats')
# what is the object type?
type(list_of_dfs)
# how many dataframes?
len(list_of_dfs)
# have a look at the first DataFrame
list_of_dfs[0]
# have a look at the second DataFrame
list_of_dfs[1]

# it would be better if we read in the top row as the column headers and the first column as the index.

list_of_dfs_nicer = pd.read_html('https://www.ussoccer.com/uswnt-stats', header=0, index_col=0)
list_of_dfs_nicer[0].head(2)
# Let's save each DataFrame as its own variable.
runners_df = list_of_dfs_nicer[0]
goalies_df = list_of_dfs_nicer[1]
# slicing DataFrames
runners_df = runners_df.iloc[:-3]
runners_df.tail(2)

goalies_df = goalies_df.iloc[:-2]
goalies_df
# make a visualization
goal_scorers_df = runners_df[runners_df['G']>0]
goal_scorers_df['G'].sort_values().plot(kind='barh', title='2020 USWNT Goals');
