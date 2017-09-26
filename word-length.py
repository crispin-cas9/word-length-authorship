# Authorship/stylometry analysis using word length
# based on a technique by TC Mendenhall (1901)

import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import urllib2
# urllib2.urlopen("http://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt")

authornames = ['Anon', 'Marlowe', 'Finley', 'Bacon', 'Earl of Oxford', 'Shakespeare', 'Wilkins', 'Sidney']
textlist = ['leir', 'marlowe', 'finley', 'bacon', 'oxford', 'shakes', 'wilkins', 'sidney']

filelist = []

for text in textlist:
	filelist.append(open ('data/' + text + '.txt'))


# match all words with 1 or more caps: [A-Z]{2}[A-Z]* (substitute that with a space)
# then match all words and use that as the data

def strip(text):
	rawdata = text.read()
	data = re.sub(r"[A-Z]{2}[A-Z]*", ' ', rawdata)
	data = re.findall(r"[a-zA-Z']+", data)
	return data

# in findper:
# numlist is the list of word lengths. lenlist is how many words have a certain length. the second value in this list is how many words are 1 letter long, the third value is how many words are 2 letters long, etc
# perlist = percent of total words


def findper(text):

	wordlist = strip(text)
	numlist = []
	lenlist = []
	perlist = []

	for word in wordlist:
		length = len(word)
		numlist.append(length)

	for x in range(13):
		howmany = numlist.count(x)
		lenlist.append(howmany)
	
	del lenlist[0]

	for n in lenlist:
		divide = float(n) / float(sum(lenlist))
		percent = divide * 100
		perlist.append(percent)
	
	return perlist


letters_per_word = []
percenttotal = []
authorlist = []

for author in authornames:
	authorlist = authorlist + [author for x in range(12)]

for x in range(len(authornames)):
	letters_per_word = letters_per_word + [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for file in filelist:
	percenttotal = percenttotal + findper(file)

graphdict = {'letters per word': letters_per_word, 'percent of total words': percenttotal, 'author': authorlist}

# the dataframe

graphdf = pd.DataFrame(graphdict)

# the graph

sns.set(style="whitegrid")

g = sns.factorplot(x="letters per word", y="percent of total words", hue="author", data=graphdf, capsize=0, errwidth=0, palette="hls", size=8, aspect=.9)
g.despine(left=True)

plt.show()

