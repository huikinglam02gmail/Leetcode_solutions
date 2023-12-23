#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#

# @lc code=start
import bisect
import heapq


class Solution:    
    '''
    First find all indices of appearance of each character.
    Then go from 'a' to 'z':
    Starting from the leftmost appearance of 'a', we ask if we have the whole set of 'b', 'c', ...., 'z' after that index. If not, we need to go to 'b' first
    '''
    def canUseThisCharacter(self, i):
        ind = self.appear[i][bisect.bisect_left(self.appear[i], self.lastUsedIndex)]
        for j in range(len(self.appear)):
            if j != i and len(self.appear[j]) > 0 and bisect.bisect_left(self.appear[j], ind) == len(self.appear[j]):
                return False
        self.lastUsedIndex = ind
        return True
    
    def smallestSubsequence(self, s: str) -> str:
        self.appear = [[] for i in range(26)]
        needProcess = []
        for i, c in enumerate(s):
            ind = ord(c) - ord('a')
            if len(self.appear[ind]) == 0:
                heapq.heappush(needProcess, ind)
            self.appear[ind].append(i)
    
        result = ""
        temp = []
        self.lastUsedIndex = -1
        while needProcess:
            ind = heapq.heappop(needProcess)
            if not self.canUseThisCharacter(ind):
                temp.append(ind)
            else:
                result += chr(ind + ord('a'))
                self.appear[ind].clear()
                while temp:
                    heapq.heappush(needProcess, temp.pop())
        return result
# @lc code=end

