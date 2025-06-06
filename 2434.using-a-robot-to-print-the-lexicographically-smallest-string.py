#
# @lc app=leetcode id=2434 lang=python3
#
# [2434] Using a Robot to Print the Lexicographically Smallest String
#

# @lc code=start
class Solution:
    '''
    As prescribed, let t be the stack holding the characters temporarily
    We first count all appearance of characters within s
    Then iterate from left to right
    For each character, we append it to t and reduce the count of the characters
    We write t[-1] to the result when there are no more characters larger than t[-1] in the remainder of the string    
    '''

    
    def robotWithString(self, s: str) -> str:
        counts = [0] * 26
        t = []
        result, i = "", 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
            i = min(i, ord(c) - ord('a'))
        for c in s:
            t.append(c)
            counts[ord(c)-ord('a')] -= 1
            while i < 26 and counts[i] == 0: i += 1
            while t and ord(t[-1]) - ord('a') <= i: result += t.pop()
        while t: result += t.pop()
        return result
            
# @lc code=end

