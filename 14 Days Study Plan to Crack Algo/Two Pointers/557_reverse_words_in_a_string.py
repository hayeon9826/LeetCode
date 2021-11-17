class Solution:
    def reverseWords(self, s: str) -> str:
        # split the sentence by whitespace, turning into array
        arr = s.split()
        temp = []
        for elem in arr:
            # for each elements in array, reverse the string
            temp.append(elem[::-1]) 
        # join the reversed array into string (=sentence)
        arr = ' '.join(temp)
        return arr





#  "Split the words in x by their spaces, reverse each word individually, and then join them back together with a space separator."
def reverseWords(self, s):
    return ' '.join(x[::-1] for x in s.split())

def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]
#source: https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/101909/1-line-Ruby-Python