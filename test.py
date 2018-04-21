import sys
from a import part1
from b import part2
import cPickle as pickle

fileList = sys.argv[1:]

# input: [fil1, file2]
# output: [[key1, key2], []]

# part1(None)
gett = fileList
if gett != None:
  part2(gett)
  with open('first_step') as rf:
    dict_list = pickle.load(rf)
  with open('second_step') as rf:
    dict_list = pickle.load(rf)
  final_list = []
  for dic in dict_list:
    final_list.append(dic.keys())
  final_list = final_list[41828:]
  print(final_list)
  sys.stdout.flush()
else:
  print('please give a non-empty file')
