test = open ('data/test.txt')

import re

def strip(text):
	rawdata = text.read()
	data = re.sub(r"[A-Z]{2}[A-Z]*", ' ', rawdata)
	data = re.findall(r"[a-zA-Z']+", data)
	return data

print strip(test)