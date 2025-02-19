#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#

# @lc code=start
class Solution:
    '''
    1 <= n <= 10
    feasible to dfs for the answer    
    '''
    def dfs(self, string, i):
        if i == 0: self.happy.append(string)
        else:
            candidates = ['a','b','c']
            for nxt in candidates:
                if len(string) == 0 or string[-1] != nxt:self.dfs(string + nxt, i - 1)
    
    def getHappyString(self, n: int, k: int) -> str:
        self.happy = []
        self.dfs("", n)
        if len(self.happy) < k: return ""
        else:
            self.happy.sort()
            return self.happy[k-1]
# @lc code=end

