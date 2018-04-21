import operator
from collections import defaultdict
import cPickle as pickle
import string
import numpy as np
import os
import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from a import part1

def part2(content, threshold_MI=0.001, threshold_IDF1=np.log(100), threshold_IDF2=np.log(5000), threshold_prune=10):
	def MI(ab,a,b):
		return -ab * np.log(ab)/(np.log(a)*np.log(b))
	def IDF(ttldocs, numdocs):
		return np.log(ttldocs/numdocs)

	dict_list = []
	with open('first_step') as rf:
		dict_list = pickle.load(rf)
	given = part1(content)
	dict_list += given
	# print(dict_list[0])
	# step1 = MI(dict_list[0]["renal palliative care"], dict_list[0]["renal palliative"],dict_list[0]["care"])
	# step2 = MI(dict_list[0]["renal palliative care"], dict_list[0]["renal"],dict_list[0]["palliative care"])
	# print("Doing Mutual Information step")
	THRES_MI = threshold_MI
	cnt = 0
	for dic in dict_list:
		for (a,b) in dic.items():
			if b[0] > 1:
				words = a.split(' ')
				split = 1
				while split < b[0]:
					split_a = ' '.join(words[:split])
					split_b = ' '.join(words[split:])
					if MI(dic[a][1],dic[split_a][1],dic[split_b][1]) > THRES_MI:
						dic[split_a] = ('F', dic[split_a][1])
						dic[split_b] = ('F', dic[split_b][1])
					split += 1
		# print(dic)
		for (a,b) in dic.items():
			if b[0] == 'F':
				del dic[a]
		# if cnt % 5000 == 0:
			# print(cnt)
		cnt += 1


	big_dic = defaultdict(int)
	for dic in dict_list:
		for a in dic.keys():
			big_dic[a] += 1
	# print(big_dic['patients'])
	# print(big_dic['patient'])
	# print(big_dic['treatment'])
	# print(big_dic['chronic'])
	# print(big_dic['well'])
	# print(big_dic['kidney'])
	# print(big_dic['pc'])
	# print(big_dic['disease'])
	# print(big_dic['describe'])
	# print(big_dic['months'])
	# print(big_dic['weeks'])

	# print("Doing IDF weighting step")
	size = len(dict_list)
	THRES_IDF1 = threshold_IDF1
	THRES_IDF2 = threshold_IDF2 * 0.01
	cnt = 0


	for dic in dict_list:
		for (a,b) in dic.items():
			idf_w1 = IDF(size, big_dic[a])
			idf_w2 = IDF(size, big_dic[a]) * b[1]
			if idf_w1 < THRES_IDF1 or idf_w2 < THRES_IDF2:
				del dic[a]
		# if cnt % 5000 == 0:
			# print(cnt)
		cnt += 1

	
	# print("Doing final pruning based on word length & frequency")
	dict_new = []
	cnt = 0
	THRES_P = threshold_prune
	for dic in dict_list:
		if len(dic) > THRES_P:
			arr = [(a,b) for (a,b) in dic.items()]
			arr = sorted(arr, key=lambda x:x[1][0],reverse=True)
			arr = sorted(arr, key=lambda x:x[1][1],reverse=True)
			arr = arr[:THRES_P]
			dict_new.append({a: b for (a,b) in arr})
		else:
			dict_new.append(dic)
		# if cnt % 5000 == 0:
			# print(cnt)
		cnt += 1

	with open('second_step','w') as wf:
		pickle.dump(dict_new, wf)
		# print("stored in \"second_step\"!")

if __name__ == '__main__':
	part2(["hello, world\nyes, sir\ncs410\ntext editor"])

