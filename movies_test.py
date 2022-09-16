movies = pd.read_csv('./movielens/movies.csv', sep=',')
tags = pd.read_csv('./movielens/tags.csv', sep=',')
ratings = pd.read_csv('./movielens/ratings.csv', sep=',', parse_dates=['timestamp'])

del ratings['timestamp']
del tags['timestamp']

is_animation = movies['genres'].str.contains('Animation')

x = movies[is_animation]
result = []
for i in range (len(y)):
    row_0 = y.iloc[i]
    if (row_0[len(row_0)-1] == ' '):
        result.append(int(row_0[len(row_0)-6:len(row_0)-2]))
    elif (row_0[len(row_0)-1] == ')'):
        result.append(int(row_0[len(row_0)-5:len(row_0)-1]))
    else:
        result.append('unknown')
x.insert(3, 'year', result)
y1 = x[['title', 'year']].groupby('year').count()
y1

----------------------------------------------------------------------

is_animation = movies['genres'].str.contains('Animation') 
is_adventure = movies['genres'].str.contains('Adventure')

x = movies[is_animation ^ is_adventure]
y = x['title']
result = []
for i in range (len(y)):
    row_0 = y.iloc[i]
    if (row_0[len(row_0)-1] == ' '):
        result.append(int(row_0[len(row_0)-6:len(row_0)-2]))
    elif (row_0[len(row_0)-1] == ')'):
        result.append(int(row_0[len(row_0)-5:len(row_0)-1]))
    else:
        result.append(0)
x.insert(3, 'year', result)
year = int(input('please enter the begin year'))
is_above = x['year'] >= year
y1 = x[is_above]
y1


------------------------------------------------------------------------

avg_ratings = ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']
box_office = movies.merge(avg_ratings, on='movieId', how='inner')
is_animation = box_office['genres'].str.contains('Animation') 
is_adventure = box_office['genres'].str.contains('Adventure')
x = box_office[is_animation ^ is_adventure]
x
y = x['title']
result = []
for i in range (len(y)):
    row_0 = y.iloc[i]
    if (row_0[len(row_0)-1] == ' '):
        result.append(int(row_0[len(row_0)-6:len(row_0)-2]))
    elif (row_0[len(row_0)-1] == ')'):
        result.append(int(row_0[len(row_0)-5:len(row_0)-1]))
    else:
        result.append(0)
x.insert(4, 'year', result)
year = int(input('please enter the begin year'))
is_above = x['year'] >= year
rating = float(input('please enter the rating'))
is_rating = x['rating'] >= rating
y1 = x[is_above & is_rating]
y1

------------------------------------------------------------------------

tags.isnull().any()
tags = tags.dropna()
x = tags.copy()
x['tag'] = x['tag'].astype('string')
x4 = x.groupby('movieId', as_index= False).agg({'movieId':'first', 'tag':', '.join})
t = movies.merge(x4, on='movieId', how='inner')
#del t['movieId']
find_tag = input('enter the tag to search')
result = t['tag'].str.contains(find_tag)
t[result]

-------------------------------------------------------------------------

tags.isnull().any()
tags = tags.dropna()
x = tags.copy()
x['tag'] = x['tag'].astype('string')
x4 = x.groupby('movieId', as_index= False).agg({'movieId':'first', 'tag':', '.join})
avg_ratings = ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']
t = movies.merge(x4, on='movieId', how='inner')
box_office = t.merge(avg_ratings, on='movieId', how='inner')
#del t['movieId']
find_tag = input('enter the tag to search')
find_rating = float(input('enter the rating'))
is_highly_rated = box_office['rating'] >= find_rating
result = box_office['tag'].str.contains(find_tag)
box_office[result & is_highly_rated]

--------------------------------------------------------------------------
