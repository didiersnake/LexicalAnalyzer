import tokens 
from tabulate import tabulate
def detect_keywords(text):
	arr = []
	for word in text:
		if word in tokens.keywords:
			arr.append(word)
	return list(set(arr))

def detect_operators(text):
	arr = []
	for word in text:
		if word in tokens.operators:
			arr.append(word)
	return list(set(arr))

def detect_delimiters(text):
	arr = []
	for word in text:
		if word in tokens.delimiters:
			arr.append(word)
	return list(set(arr))

def detect_num(text):
	arr = []
	for word in text:
		try:
			a = int(word)
			arr.append(word)
		except:
			pass
	return list(set(arr))

def detect_identifiers(text):
	k = detect_keywords(text)
	o = detect_operators(text)
	d = detect_delimiters(text)
	n = detect_num(text)
	not_ident = k + o + d + n
	arr = []
	for word in text:
		if word not in not_ident:
			arr.append(word)
	return arr

with open('test.txt') as t:
	text = t.read().split()
print("Table of tokens")
headers = ['Keywords', 'Operators', 'Delimiters', 'Identifiers', 'Numbers']
table = zip(detect_keywords(text), detect_operators(
	text), detect_delimiters(text), detect_identifiers(text), detect_num(text))
print(tabulate(table, headers=headers, floatfmt=".4f"))

