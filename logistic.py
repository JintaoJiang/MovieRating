import numpy as np

trains = open('new_trains.txt', 'r').read().split('\n')[1:-1]
col = len(trains[0].split(',')) - 1
row = len(trains)
ratings = np.zeros(row)
features = np.zeros((row, col))
for train_num, train in enumerate(trains):
	train = train.split(',')[1:]
	ratings[train_num] = train[-1]
	train = train[:-1]
	features[train_num][0] = 1.0
	for num, tra in enumerate(train):
		features[train_num][num + 1] = float(tra)

thetas = [np.zeros(col)] * 5
learning = 0.1
for idx, theta in enumerate(thetas):
	i = 0
	ratings_tmp = np.zeros(row)
	for num, rate in enumerate(ratings):
		if rate == idx + 1:
			ratings_tmp[num] = 1
	while True:
		H = 1 / (1 + np.exp(-theta.dot(features.transpose())))
		J = sum(- ratings_tmp * np.log(H) - (1 - ratings_tmp) * np.log(1 - H)) / row 
		print(J)
		i += 1
		if J == 0 or i == 10:
			break
		theta = theta - learning / row * sum(((H - ratings_tmp) * features.transpose()).transpose())
	thetas[idx] = theta

tests = open('new_tests.txt', 'r').read().split('\n')[1:-1]
col2 = len(tests[0].split(','))
row2 = len(tests)
ratings2 = np.zeros(row2)
features2 = np.zeros((row2, col2))
for test_num, test in enumerate(tests):
	test = test.split(',')[1:]
	features2[test_num][0] = 1.0
	for num, te in enumerate(test):
		features2[test_num][num + 1] = float(te)
for theta in thetas:
	ratings2 = np.vstack((ratings2, (1 / (1 + np.exp(-theta.dot(features2.transpose()))))))
ratings2 = ratings2[1:]
print(ratings2)
ratings3 = 1 + np.argmax(ratings2, 0)
print(ratings3)
samples = open('sample2.txt', 'w')
samples.write('Id,rating\n')
for i in range(len(tests)):
	samples.write(''.join([tests[i].split(',')[0], ',', str(ratings3[i])[0], '\n']))
