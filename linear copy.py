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

theta = np.zeros(col)
learning = 0.05
i = 0
while True:
	J = sum((theta.dot(features.transpose()) - ratings) ** 2) / row
	print(J)
	i += 1
	if J == 0 or i == 100:
		break
	theta = theta - learning / row * sum(((theta.dot(features.transpose()) - ratings) * features.transpose()).transpose())

tests = open('new_tests.txt', 'r').read().split('\n')[1:-1]
col2 = len(tests[0].split(','))
row2 = len(tests)
ratings2 = np.zeros(row2)
features2 = np.zeros((row2, col2))
for test_num, test in enumerate(tests):
	test = test.split(',')[1:-1]
	features2[test_num][0] = 1.0
	for num, te in enumerate(test):
		features2[test_num][num + 1] = float(te)
ratings2 = np.around(theta.dot(features2.transpose()))
ratings2.astype(int)
samples = open('sample.txt', 'w')
samples.write('Id,rating\n')
for i in range(len(tests)):
	if ratings2[i] > 5:
		samples.write(''.join([tests[i].split(',')[0], ',', '5', '\n']))
	elif ratings2[i] < 1:
		samples.write(''.join([tests[i].split(',')[0], ',', '1', '\n']))
	else:
		samples.write(''.join([tests[i].split(',')[0], ',', str(ratings2[i])[0], '\n']))
