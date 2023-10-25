#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    '''
    nth row total number of nodes = 2^(n-1)
    kth element in (n-1)th row will lead to (2*k-1) and 2*k th element in row k
    Therefore for kth element in nth row, we first ask if it is odd or even.
    if odd, we ask if f(n-1, (k+1) // 2) is 0. it will be 0. else it will be 1
    if even, we return f(n-1, k // 2) is 0, it will be 1, else it will 0    
    '''
    def kthGrammar(self, n: int, k: int) -> int:
        return int((n > 1 or k > 1) and (1 - (k % 2) ^ self.kthGrammar(n - 1, (k + 1) // 2)))       
# @lc code=end

