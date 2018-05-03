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

stemmer = SnowballStemmer('english')

# THRES = 1
stopwords = set(stopwords.words('english'))

def get_abbr(tokens, abbr_dict):
    new_dict = {}
    for i in range(len(tokens)):
        abbr = re.findall("^\(\S+\)$", tokens[i])
        if abbr:
            found = abbr[0][1:-1]
            derive_len = len(found.translate(None, "-_0123456789"))
            start = i - derive_len
            if start < 0:
                start = 0
            for j in range(start, i):
                if tokens[j][0].lower() == found[0].lower():
                    string_found = ' '.join(tokens[j:i])
                    if found in new_dict.keys():
                        new_dict[found].append(string_found)
                    else:
                        new_dict[found] = [string_found]
                break
    tokens = [x for x in tokens if not re.findall("^\(\S+\)$", x)]
    for i in range(len(tokens)):
        if tokens[i] in new_dict.keys():
            tokens[i] = new_dict[tokens[i]][0]

    new_doc = ' '.join(tokens)
    for key in new_dict.keys():
        if key in abbr_dict.keys():
            abbr_dict[key].append(new_dict[key])
        else:
            abbr_dict[key] = new_dict[key]
    return new_doc
    
                
def tokenize(document, abbr_dict):
    if document is None:
        return None
    
    tokens = document.translate(None, "!\"#$%&\'*+,.:;<=>?@[\]^`{|}~").split()
    
    new_document = get_abbr(tokens, abbr_dict)
#     tokens = new_document.split()
    
#     for i in range(len(tokens)):
#         if tokens[i].upper() != tokens[i]:
#             tokens[i] = tokens[i].lower()
    return new_document



def check_combine(document, tf, last_tf,THRES,size,num_tok):
    this_tf = defaultdict(int)

    for a in tf:
        for b in last_tf:
            phrase1 = a + ' ' + b
            count1 = document.count(phrase1)
            phrase2 = b + ' ' + a
            count2 = document.count(phrase2)
            if count1 > THRES:
                this_tf[phrase1] = (num_tok, 1.0*count1/size)
            if count2 > THRES:
                this_tf[phrase2] = (num_tok, 1.0*count2/size)
    return this_tf


def build_tf(document,threshold,abbr_dict):
    tf = defaultdict(int)
    token_list = tokenize(document,abbr_dict)
    for token in token_list:
        token = token.rstrip().lstrip()
        # word = token.replace(",", "")
        # word = word.replace(".", "")
        # word = word.replace("(", "")
        # word = word.replace(")", "")
        # word = word.replace(":", "")
        if token not in stopwords and token != '' and not token.isdigit():
            tf[token] += 1
    size = len(token_list) * 1.0
    THRES = threshold * size

    for (a,b) in tf.items():
        if b <= THRES:
            del tf[a]
        else:
            tf[a] = (1,b/size)

    last_tf = tf
    multi_level_tf = []
    num_tok = 2
    while True:
        new_tf = check_combine(document, tf, last_tf, THRES, size, num_tok)
        if len(new_tf) == 0:
            break
        last_tf = new_tf
        multi_level_tf.append(new_tf)
        num_tok += 1
    
    for t in multi_level_tf:
        for p in t:
            tf[p] = t[p]


    return tf



def part1(cont,threshold=0.01):
	content = None
	if cont == None:
		with open('pmid2meta_autophrase.chunk0') as f:
			content = f.readlines()
	else:
		content = cont
	# print(content[10764])

	dict_list = []
	count = 0
	# print("Doing frequent pattern mining")
	for document in content:
		if document[-1] == '\n':
			document = document[:-1]
		tf = build_tf(document,threshold)
		# print(tf)
		# sorted_tf = sorted(tf.items(), key=operator.itemgetter(1), reverse=True)
		# print(sorted_tf)
		dict_list.append(tf)
		# if count % 5000 == 0:
			# print(count)
		count += 1
	if cont == None:
		with open('first_step','w') as wf:
			pickle.dump(dict_list,wf)
			# print("stored in \"first_step\"!")
		return None
	else:
		return dict_list
if __name__ == '__main__':
	part1(None)

