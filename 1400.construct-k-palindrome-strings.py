#
# @lc app=leetcode id=1400 lang=python3
#
# [1400] Construct K Palindrome Strings
#

# @lc code=start
class Solution:
    '''
    This problem is less complicated than it appears
    Just break it down logically, think about when it should return False
    if k > len(s): return False
    if count of odd appearance > k: return False
    Otherwise return True    
    '''
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        counts = [0]*26
        for c in s: counts[ord(c)-ord('a')] += 1
        odds = 0
        for i in range(26):
            if counts[i] % 2 == 1: odds += 1
        return odds <= k
# @lc code=end

