# Authorship/stylometry analysis using word length
# based on a technique by TC Mendenhall

import urllib2
import re

shakes = urllib2.urlopen("http://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt")
leir = open ('data/leir.txt')
marlowe = open ('data/faustus.txt')
test = open ('data/test.txt')

def strip(text):
	rawdata = text.read().lower()
	data = re.findall(r"[\w']+", rawdata)
	return data

wordlist = strip(marlowe)
numlist = []
lenlist = []
perlist = []

for word in wordlist:
	length = len(word)
	numlist.append(length)

# numlist is the list of word lengths. lenlist is how many words have a certain length. the second value in this list is how many words are 1 letter long, the third value is how many words are 2 letters long, etc

for x in range(13):
	howmany = numlist.count(x)
	lenlist.append(howmany)

for n in lenlist:
	divide = float(n) / float(sum(lenlist))
	percent = divide * 100
	perlist.append(percent)

#print numlist
#print lenlist
print perlist



