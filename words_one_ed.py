"""
Function to generate a list of all words that are 1 edit distance from the given word.
Output may contain duplicates.

Inputs:
str1 -- input string to generate words 1 edit distance away.
input_set -- optional arg. defaults to ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

Other helpful sets:
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789

Usage:
from words_one_ed import words_one_ed
words_one_ed("abc", "xy")
"""

import string

# toy example: print(words_one_ed("abc", "xy"))
def words_one_ed(str1, input_set=string.ascii_letters):

    """ words_one_ed("abc", "") == ['bc', 'ac', 'ab'] """
    """ words_one_ed("abc", "xy") == ['xabc', 'yabc', 'axbc', 'aybc', 'abxc', 'abyc', 'abcx', 'abcy', 'bc', 'ac', 'ab', 'xbc', 'ybc', 'axc', 'ayc', 'abx', 'aby']"""
    """ words_one_ed("", "xy") == ['x', 'y'] """
    """ words_one_ed("", "") == [] """

    # error checking
    if input_set == None:
        raise ValueError("argument input_set is invalid")

    out = []

    n = len(str1)
    
    #additions
    for i in range(n+1):
        out.extend(add_char(str1, i, input_set)) # using extend because add_char returns a list

    #deletions
    for i in range(n):
        out.append(remove_char(str1, i)) # append because remove_char return a word

    #replacements
    for i in range(n):
        out.extend(replace_char(str1, i, input_set)) # using extend because replace_char returns a list

    
    return out


# add a char from inp_set between x[0:idx] and x[idx::]
# print(add_char("abc", 3, "xy"))
def add_char(x, idx, inp_set):

    if(idx < 0 or idx > len(x)):
        raise ValueError("input arg idx is not within valid bounds to add char")

    out = []

    for i in range(len(inp_set)):
        out.append(x[0:idx] + inp_set[i] + x[idx::])

    return out

# remove char x[idx]
# print(remove_char("abc", 0))
def remove_char(x, idx):
    if len(x) == 0:
        return ""

    if(idx < 0 or idx >= len(x)):
        raise ValueError("input arg idx is not within bounds of input string x")

    return x[0:idx] + x[idx+1::]

# replace char x[idx] with chars in inp_set
# print(replace_char("abc", 2,"xy"))
def replace_char(x, idx, inp_set):
    if(idx < 0 or idx >= len(x)):
        raise ValueError("input arg idx is not within bounds of input string x")

    out = []

    for i in range(len(inp_set)):
        out.append(x[0:idx] + inp_set[i] + x[idx+1::])

    return out



# print(add_char("abc", 3, "xy"))
# print(remove_char("abc", 0))
# print(replace_char("abc", 2,"xy"))

# print(words_one_ed("abc", "xy"))