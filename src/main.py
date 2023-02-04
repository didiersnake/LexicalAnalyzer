import tokens
from tabulate import tabulate


# ==== Detect Keywords ====
def detect_keywords(text):
    """
    Detects the keywords in source language scripts

    Args:
        text (string): A string representing the source language code to be analysed

    Returns:
        Array : An array of all the keywords detected in the text passed as Argument
    """
    arr = []
    for word in text:
        if word in tokens.keywords:
           arr.append(word)
    return list(set(arr))

# ==== Detect operators ====
def detect_operators(text):
    """
    Detects the operators in source language scripts

    Args:
        text (string): A string representing the source language code to be analysed

    Returns:
        Array : An array of all the operators detected in the text passed as Argument
    """
    arr = []
    for word in text:
        if word in tokens.operators:
            arr.append(word)
    return list(set(arr))

# ==== Detect delimiters ====
def detect_delimiters(text):
    """
    Detects the Delimiters in source language scripts

    Args:
        text (string): A string representing the source language code to be analysed

    Returns:
        Array : An array of all the delimiters detected in the text passed as Argument
    """
    arr = []
    for word in text:
        if word in tokens.delimiters:
            arr.append(word)
    return list(set(arr))

# ==== Detect numbers ====
def detect_num(text):
    """
    Detects the numbers in source language scripts

    Args:
        text (string): A string representing the source language code to be analysed

    Returns:
        Array : An array of all the numbers detected in the text passed as Argument
    """
    arr = []
    for word in text:
        try:
            a = int(word)
            arr.append(word)
        except:
            pass
    return list(set(arr))

# ==== Detect identifiers ====
def detect_identifiers(text):
    """
    Detects the identifiers in source language scripts

    Args:
        text (string): A string representing the source language code to be analysed

    Returns:
        Array : An array of all the identifiers detected in the text passed as Argument
    """
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

with open('src/test.txt') as t:
	text = t.read().split()
print("----Table of tokens----")
print("Column of tokens and rows of lexemes")
headers = ['Keywords', 'Operators', 'Delimiters', 'Identifiers', 'Numbers']
table = zip(detect_keywords(text), detect_operators(
	text), detect_delimiters(text), detect_identifiers(text), detect_num(text))
print(tabulate(table, headers=headers, floatfmt=".4f"))

