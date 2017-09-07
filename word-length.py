# Authorship/stylometry analysis using word length
# based on a technique by TC Mendenhall

import urllib2
import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

shakes = urllib2.urlopen("http://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt")
leir = open ('data/leir.txt')
marlowe = open ('data/faustus.txt')
test = open ('data/test.txt')

def strip(text):
	rawdata = text.read().lower()
	data = re.findall(r"[\w']+", rawdata)
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

	for n in lenlist:
		divide = float(n) / float(sum(lenlist))
		percent = divide * 100
		perlist.append(percent)
	
	return perlist

per_shakes = findper(shakes)
per_leir = findper(leir)
per_marlowe = findper(marlowe)

letters_per_word = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# graphdict = {'letters per word': ['1', '3'], 'percent of total words': ['1', '2'], 'author': ['2', '4']}

# print(pd.DataFrame(graphdict))



