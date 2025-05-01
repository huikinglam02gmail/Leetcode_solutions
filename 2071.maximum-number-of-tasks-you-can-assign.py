#
# @lc app=leetcode id=2071 lang=python3
#
# [2071] Maximum Number of Tasks You Can Assign
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use binary search to find the largest k in which tasks[:k] can be completed with workers[-k:], given both of them are sorted:
    if tasks[j] <= sl[-1]: use the largest  
    '''

    def canFinish(self, k, pills):
        sl = SortedList(self.workers[-k:])
        for j in range(k - 1, -1, -1):
            if self.tasks[j] <= sl[-1]: sl.pop()
            elif pills == 0: return False
            else:
                ind = sl.bisect_left(self.tasks[j] - self.strength)
                if ind == len(sl): return False
                else:
                    pills -= 1
                    sl.pop(ind)
        return True
            
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        self.tasks = tasks
        self.workers = workers
        self.strength = strength
        self.workers.sort()
        self.tasks.sort()

        l, r = 0, min(len(self.workers), len(self.tasks)) + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.canFinish(mid, pills): l = mid + 1
            else: r = mid
        return l - 1

# @lc code=end

