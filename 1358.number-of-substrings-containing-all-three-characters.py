#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    '''
    sliding window
    loop right, initialize left at 0
    if we reach our target, we know right:n (n - right) substrings would satisfy
    we increment left and keep testing   
    '''

    def numberOfSubstrings(self, s: str) -> int:
        result, n, left, abc = 0, len(s), 0, [0]*3
        for right in range(n):
            abc[ord(s[right])-ord('a')] += 1
            while all([x > 0 for x in abc]):
                result += n - right
                abc[ord(s[left])-ord('a')] -= 1
                left += 1
        return result
# @lc code=end

