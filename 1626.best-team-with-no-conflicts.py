#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#

# @lc code=start
from typing import List

class MaxSegmentTree:
    def __init__(self, n, value) -> None:
        self.tree = [value]*n

    def update(self, i, val):
        i += len(self.tree) // 2
        self.tree[i] = val
        i //= 2
        while i > 0:
            self.tree[i] = max(self.tree[2*i], self.tree[2*i + 1])
            i //= 2
    
    def query(self, i, j):
        i += len(self.tree) // 2
        j += len(self.tree) // 2
        s = 0
        while i <= j:
            if i % 2 == 1:
                s = max(s, self.tree[i])
                i += 1
            if j % 2 == 0:
                s = max(s, self.tree[j])
                j -= 1
            i //= 2
            j //= 2
        return s 

class Solution:
    # We first group the data together in terms of [score, age]
    # Then sort them by score then by age
    # Then for each item, we keep adding them to a segment tree of size max(ages)
    # Because scores are nondecreasing, for each new item we ask
    # what is the maximum total score so far up to current age? Then add to it because the current score must be larger than or equal to the previous max score
  
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = MaxSegmentTree(2*(1 + max(ages)), 0)
        data = []
        result = 0
        for score, age in zip(scores, ages):
            data.append([score, age])
        data.sort()

        for score, age in data:
            maxTotalScoreSoFar = dp.query(0, age)
            newMaxTotalScoreCandidate = maxTotalScoreSoFar + score
            result = max(result, newMaxTotalScoreCandidate)
            dp.update(age, newMaxTotalScoreCandidate)
        return result


# @lc code=end

