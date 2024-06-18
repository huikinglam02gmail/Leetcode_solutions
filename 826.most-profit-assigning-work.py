#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    '''
    sort difficulty, pair up difficulty with profit (diff_prof)
    Then run through diff_prof from the left to give the maxsofar seen
    Then for each worker, binary search for index in which work on the left is doable. Add the corresponding maxsofar    
    '''
    
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_prof = []
        for i in range(len(difficulty)):
            diff_prof.append([difficulty[i], profit[i]])
        diff_prof.sort(key = lambda x: x[0])
        max_profit = []
        max_so_far = 0
        for i in range(len(difficulty)):
            max_so_far = max(max_so_far, diff_prof[i][1])
            max_profit.append(max_so_far)
        result = 0
        for person in worker:
            l = bisect.bisect_right(diff_prof, person, key = itemgetter(0))
            if l > 0:
                result += max_profit[l - 1]
        return result
# @lc code=end

