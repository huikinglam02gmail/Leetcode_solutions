#
# @lc app=leetcode id=1982 lang=python3
#
# [1982] Find Array Given Subset Sums
#

# @lc code=start
from typing import List


class Solution:
    '''
    Suppose we have [1, 2], we have subset sum = {0, 1, 2, 3}
    Then we add -3: the subset sum becomes: {0, 1, 2, 3, 0 - 3, 1 - 2, 2 - 3, 3 - 3}
    So given sums, our task is to separate it into two groups in which if x is the newly added element, we have two groups:
    left, [l + x for l in left]
    If we sort sums, we can recover the numbers by order by abs(num) as we can extract x from sums[1] - sums[0]. x could be either sums[1] - sums[0] or sums[0] - sums[1], depending on which side consider the subset sum of 0 (empty set)
    '''
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        if n == 0:
            return []
        else:
            sums.sort()
            x = sums[1] - sums[0]
            left, right = [], []
            indLeft = 0
            for s in sums:
                if 0 <= indLeft < len(left) and s - x == left[indLeft]:
                    right.append(s)
                    indLeft += 1
                else:
                    left.append(s)
            if 0 in left:
                return [x] + self.recoverArray(n - 1, left)
            else:
                return [- x] + self.recoverArray(n - 1, right)

        
# @lc code=end

