# Authorship/stylometry analysis using word length
# based on a technique by TC Mendenhall (1901)

import urllib2
import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

shakesall = urllib2.urlopen("http://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt")
shakes = open ('data/shakes.txt')
leir = open ('data/leir.txt')
marlowe = open ('data/marlowe.txt')
test = open ('data/test.txt')
finley = open ('data/finley.txt')
wilkins = open ('data/wilkins.txt')
pericles = open ('data/pericleshalf.txt')
bacon = open ('data/bacon.txt')
oxford = open ('data/oxford.txt')
sidneyprose = open ('data/sidneyprose.txt')
sidneyverse = open ('data/sidneyverse.txt')
sidney = open ('data/sidney.txt')

# add sidney verse and prose!

def strip(text):
	rawdata = text.read()
	data = re.sub(r"[A-Z]{2}[A-Z]*", ' ', rawdata)
	data = re.findall(r"[a-zA-Z']+", data)
	return data

# match all words with 1 or more caps: [A-Z]{2}[A-Z]*

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


# for each new author added: add a variable for the findper output of the text, a number to "range," the author name to "authorlist," the findper variable to percenttotal, categories

per_shakes = findper(shakes)
per_leir = findper(leir)
per_marlowe = findper(marlowe)
per_finley = findper(finley)
per_wilkins = findper(wilkins)
per_pericles = findper(pericles)
per_bacon = findper(bacon)
per_oxford = findper(oxford)
per_sverse = findper(sidneyverse)
per_sprose = findper(sidneyprose)
per_sidney = findper(sidney)

letters_per_word = []
authorlist = []

for x in range(8):
	letters_per_word = letters_per_word + [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

authorlist = ['Anon' for x in range(12)] + ['Marlowe' for x in range(12)] + ['Finley' for x in range(12)] + ['Bacon' for x in range(12)] + ['Earl of Oxford' for x in range(12)] + ['Shakespeare' for x in range(12)] + ['Wilkins' for x in range(12)] + ['Sidney' for x in range(12)]

percenttotal = per_leir + per_marlowe + per_finley + per_bacon + per_oxford + per_shakes + per_wilkins + per_sidney

graphdict = {'letters per word': letters_per_word, 'percent of total words': percenttotal, 'author': authorlist}

# the dataframe

graphdf = pd.DataFrame(graphdict)

# the graph

sns.set(style="whitegrid")

g = sns.factorplot(x="letters per word", y="percent of total words", hue="author", data=graphdf, capsize=0, errwidth=0, palette="hls", size=8, aspect=.9)
g.despine(left=True)

plt.show()



