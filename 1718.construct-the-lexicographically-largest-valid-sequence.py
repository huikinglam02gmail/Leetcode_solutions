#
# @lc app=leetcode id=1718 lang=python3
#
# [1718] Construct the Lexicographically Largest Valid Sequence
#

# @lc code=start
from typing import List


class Solution:
    '''
    Put the integers in from left to right, and from large to small. Whenver we can fill the array, we have the answer
    '''                

    def backtrack(self, i):
        if i == 2*self.n - 1:
            self.ans = [num for num in self.arr]
            return True
        elif self.arr[i] > 0:
            return self.backtrack(i + 1)
        else:
            for j in range(self.n, 0, -1):
                if j not in self.used and (j == 1 or (i + j < 2*self.n - 1 and self.arr[i + j] == 0)):
                    self.used.add(j)
                    self.arr[i] = j
                    if j > 1: self.arr[i + j] = j
                    if self.backtrack(i + 1): return True
                    self.arr[i] = 0
                    if j > 1: self.arr[i + j] = 0
                    self.used.remove(j)
            return False


    def constructDistancedSequence(self, n: int) -> List[int]:
        self.arr = [0 for i in range(2*n - 1)]
        self.used = set()
        self.n = n
        self.ans = []
        found = self.backtrack(0)
        return self.ans
        

            
# @lc code=end
