#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS starting with 1-9
    Stop when the number is too large    
    '''
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        dq, result = deque(), []
        for i in range(1,10): dq.append(i)
        while dq:
            num = dq.popleft()
            if low <= num <= high: result.append(num)
            if num <= high and num % 10 < 9: dq.append(num*10 + (num % 10 + 1))
        return sorted(result)
# @lc code=end

