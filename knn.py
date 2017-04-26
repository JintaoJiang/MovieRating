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

tests = open('new_tests.txt', 'r').read().split('\n')[1:-1]
samples = open('sample3.txt', 'w')
samples.write('Id,rating\n')
for test in tests:
	test = test.split(',')
	test_id = test[0]
	test = test[1:]
	test_tmp = np.zeros(len(test) + 1)
	test_tmp[0] = 1.0
	for num, te in enumerate(test):
		test_tmp[num + 1] = float(te)
	ret = sum((np.abs(features - test_tmp)).T)
	ret = ratings[np.argpartition(ret, 10)[:10]]
	ret2 = np.zeros(10, dtype = np.int)
	for num, re in enumerate(ret):
		ret2[num] = int(re)
	count = np.bincount(ret2)
	ret3 = np.argmax(count)
	samples.write(''.join([test_id, ',', str(ret3), '\n']))

