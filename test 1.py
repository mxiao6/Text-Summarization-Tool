from a import part1
from b import part2
import operator
from collections import defaultdict
import cPickle as pickle
import os
import sys
import numpy as np

def main():
	part1()
	part2()
	with open('second_step') as rf:
		dict_list = pickle.load(rf)
	final_list = []
	for dic in dict_list:
		final_list.append(dic.keys())

if __name__ == '__main__':
	main()