"""
Function to compute edit distance between two words.
Edit distance -- the minimum number of +, -, r operations that are needed to convert str2 to str1.
+, -, r are addition, subtraction and replacement.

For example: 
str1 = "abc", str2 = "ac". edit distance is 1 --> addition of b str2.
str1 = "abc", str2 = "axc". edit distance is 1 --> replace x with b in str2.
str1 = "a", str2 = "xc". edit distance is 2 --> remove c, replace x with a.

str1 -- first input string.
str2 -- second input string.
out -- edit distance. 

usage: 
from edit_distance import edit_distance
edit_distance(str1, str2)
"""
import numpy as np

def edit_distance(str1, str2):

    """ edit_distance("", "") == 0 """
    """ edit_distance("a", "") == 1 """
    """ edit_distance("", "a") == 1 """
    """ edit_distance("b", "a") == 1 """
    """ edit_distance("xyz", "abc") == 3 """

    # get length of str1 and str2
    n1 = len(str1)
    n2 = len(str2)

    #create a 2d array
    dp = np.zeros(shape=(n2+1, n1+1)).astype('int')
    
    #dp[0][0] is the distance between two empty strings. Hence 0.
    dp[0][0] = 0 # redundant but for clarity

    #initialize the dp array
    for i1 in range(1, n1+1):
        # edit distance of empty string to another string of length i1 is i1.
        dp[0][i1] = i1

    for i2 in range(1, n2+1):
        # edit distance of a string of length i2 to be converted to empty is i2
        dp[i2][0] = i2


    # dp for non trivial strings
    for i1 in range(1, n1+1):
        for i2 in range(1, n2+1):
            if(str1[i1-1] == str2[i2-1]): 
                # if the characters are the same, then get the distance from prefixes of both str1 and str2
                dp[i2][i1] = dp[i2-1][i1-1]
            else:
                dp[i2][i1] = np.min([ dp[i2-1][i1-1] +1, # replacing str2[i2] with str1[i1]
                                      dp[i2-1][i1] +1, # remove str2[i2]
                                      dp[i2][i1-1] +1 ]) # add str1[i1] at the end

    
    out = dp[n2][n1]

    return out