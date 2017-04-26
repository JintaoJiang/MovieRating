#rearrange the movie in order
movies = open('movie.txt', 'r').read().split('\n')[1:-1]
new_movies = open('new_movie.txt', 'w')
movies = sorted(movies, key = lambda a : int(a.split(',')[0]))
new_movies.write('Id,Year,Genre\n')
for movie in movies:
	new_movies.write(movie + '\n')
#add genre to the last line
genre = []
for movie in movies:
	movie = movie.split(',')
	movie = movie[2].split('|')
	for mov in movie:
		if mov not in genre and mov != 'N/A':
			genre.append(mov)
out = ''
for gen in genre:
	out = ''.join([out, gen, ','])
new_movies.write(out[:-1])