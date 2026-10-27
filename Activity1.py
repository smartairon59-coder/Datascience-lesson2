import pandas as pd 

# PART ! - Create a Pandas  Series of top player scores
print('- - - PART 1: PANDAS Series - - -')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=['NightWolf', 'starBlaze', 'PixelKing', 'CyberFox', 'IronStorm'])
print(players)

# PART 2 - Create a Dataframe fo gaming stats
print()
print(' - - - PART 2: Pandas DataFrame - - -')
data ={
    'Player':  ['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'Ironstorm'],
    'Level': [42, 38, 35, 30, 27],
    'Score':[98500, 87200, 76400, 65100, 54800],
    'Wins': [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)

# PART # - Access rows using .loc
print()
print('- - - PART#: Acessing Rows - - -')
print('Row 0 (top player):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])

# PART $ - Load leaderboard.csv and view the data
print()
print('- - - PART 4: READING a CSV File - - -')
full_df = pd.read_csv('leaderboard.csv')
print('First 5 rows (head):')
print()
print('Last 3 rows (tail):')
print(full_df.tail(3))
print()
print('Dataset info:')
print(full_df.info())

# PART 5 - Clean the data
print()
print('- - - PART 5: Cleaning Data - - -')
print('Rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('Missig Values filled with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())