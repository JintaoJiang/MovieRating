#put features together
users = open('user.txt', 'r').read().split('\n')[1:-1]
movies = open('new_movie.txt', 'r').read().split('\n')[1:]
trains = open('train.txt', 'r').read().split('\n')[1:-1]
new_trains = open('new_trains.txt', 'w')

Genre = movies[-1]
movies = movies[:-1]
new_trains.write(''.join(['Id,Gender,Age,Occupation,Year,', Genre, ',Rating\n']))
Genre = Genre.split(',')
for train in trains:
	train = train.split(',')
	Id = train[0]
	userid = int(train[1])
	movieid = int(train[2])
	rating = train[3]
	user = users[userid].split(',')
	gender = user[1]
	age = user[2]
	occupation = user[3]

	#there's skip in the movie id
	year = ''
	genre = ''
	small = 0
	large = len(movies)
	while True:
		i = int((small + large) / 2)
		check = int(movies[i].split(',')[0])
		if check == movieid:
			year = movies[i].split(',')[1]
			genre = movies[i].split(',')[2]
			break
		elif check < movieid:
			small = i
		else:
			large = i
	genre = genre.split('|')
	genre_list = ''
	for gen in Genre:
		if gen in genre:
			genre_list = ''.join([genre_list, '1', ','])
		else:
			genre_list = ''.join([genre_list, '0.1', ','])
	genre_list = genre_list[:-1]

	#data preprocessing
	if gender == 'F':
		gender = '0'
	elif gender == 'T':
		gender = '1'
	else:
		gender = '0.5'
	if age == 'N/A':
		age = '0.5'
	else:
		age = str(int(age) / 50)
	if occupation == 'N/A':
		occupation = '0.5'
	else:
		occupation = str(int(occupation) / 20)
	if year == 'N/A':
		year = '0.5'
	else:
		year = str((int(year) - 1900) / 100)

	new_trains.write(''.join([Id, ',', gender, ',', age, ',', occupation, ',', year, ',', genre_list, ',', rating, '\n']))
