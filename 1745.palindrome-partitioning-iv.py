#
# @lc app=leetcode id=1745 lang=python3
#
# [1745] Palindrome Partitioning IV
#

# @lc code=start
class Solution:
    '''
    We want to cut into three non-empty palindromic substrings. It's equivalent to choosing 2 cut points l and r to split s into s[:l], s[l:r], s[r:]
    Here l > 0 and r < n and l < r
    Now we want to check whether s[i:j] for 0 <= i < j < n is palindrome. We do not want to do it when we scan l and r. So do it beforehand
    '''
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        isPalindrome = [[False for i in range(n)] for j in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    isPalindrome[i][j] = True
                elif (isPalindrome[i + 1][j - 1] or j == i + 1) and s[i] == s[j]:
                    isPalindrome[i][j] = True

        for l in range(1, n - 1):
            for r in range(l + 1, n):
                if isPalindrome[0][l - 1] and isPalindrome[l][r - 1] and isPalindrome[r][n - 1]:
                    return True
        return False
# @lc code=end

