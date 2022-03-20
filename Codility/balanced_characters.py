# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def findMatch(s):
    lower = dict(Counter( [x for x in s if x.lower() == x] ))
    upper = dict(Counter( [x for x in s if x.upper() == x] ))

    match = {}

    for char in lower:
        if char.upper() in upper:
            match[char] = upper[char.upper()] + lower[char]
    
    match_char = ''.join([x if x.lower() in match else ' ' for x in s ]).split()

    return match_char


def solution(S):
    matching_char = findMatch(S)

    if len(matching_char) == 1:
        return(len(matching_char[0]))
    elif len(matching_char) == 0:
        return -1
    else:
        list_len = []
        for i in matching_char:
            list_len.append(solution(i))
        return max(list_len)



# 참고: https://stackoverflow.com/questions/68735445/smallest-window-substring-that-has-both-uppercase-and-corresponding-lowercase

# I'm using a recursive approach to this; I'm not sure what it's time complexity is though.

# The idea is we check what characters in the string are present in both their lower and upper form formats. For any characters that aren't given in both forms, we replace them with a space ' '. We then split the remaining string on ' ' into a list.

# In the first case, if we have only one string left after it- we return it's length.

# In the second case, if we have no characters left, we return -1.

# In the third case, if we have more than one string left, we re-evaluate each of the strings sub-lengths and return the length of the longest string we then evaluate.