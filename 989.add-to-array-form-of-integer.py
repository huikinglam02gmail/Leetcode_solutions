#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
from typing import List


class Solution:
    # We can pop out the last element from num one by one, and apply the addition
    # For example, num = [2,1,5], first we pop 5 and add k%10 = 6 to it. That will give 11 and therefore the we have the digit one and passover of 1
    # We put the digit into a new array
    # In the end we return reverse of the new array
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        passover, result = 0, []
        while num:
            ele = num.pop()
            k, d = divmod(k, 10)
            passover, new = divmod(ele + d + passover, 10)
            result.append(new)
        while k > 0:
            k, d = divmod(k, 10)
            passover, new = divmod(d + passover, 10)
            result.append(new)
        if passover > 0:
            result.append(1)
        return reversed(result)
            
# @lc code=end

