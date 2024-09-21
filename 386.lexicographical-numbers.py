#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
from typing import List


class Solution:
    '''
    iterate from 1, multiply 10 and ask if the num > n. If so, divide by 10 and += 1
    '''
    def lexicalOrder(self, n: int) -> List[int]:
        result = [1]
        while len(result) < n:
            next = result[-1] * 10
            while next > n:
                next //= 10
                next += 1
                while not next % 10: next //= 10
            result.append(next)
        return result

        
# @lc code=end

