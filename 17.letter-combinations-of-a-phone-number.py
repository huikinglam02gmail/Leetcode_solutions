#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def dfs(self, pos, string):
        if pos == len(self.digits):
            if string: 
                self.result.append(string)
        else:
            s = self.hash_table[self.digits[pos]]
            for c in s:
                self.dfs(pos + 1, string + c)
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.hash_table ={"2": "abc","3":"def", "4":"ghi", "5":"jkl" , "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        self.result = []
        self.digits = digits
        
        self.dfs(0,'')
        return self.result
# @lc code=end

