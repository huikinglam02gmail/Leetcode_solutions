#
# @lc app=leetcode id=2243 lang=python3
#
# [2243] Calculate Digit Sum of a String
#

# @lc code=start
from collections import deque


class Solution:
    '''
    Just simulate with a queue
    '''
    def digitSum(self, s: str, k: int) -> str:
        dq = deque()
        for c in s:
            dq.append(int(c))
        while len(dq) > k:
            count, current = 0, [0]
            while dq:
                while count < k and dq:
                    count += 1
                    current[-1] += dq.popleft()
                if dq: 
                    count = 0
                    current.append(0)
            for num in current:
                numString = str(num)
                for c in numString:
                    dq.append(int(c))
        result = ""
        while dq:
            result += str(dq.popleft())
        return result
        
# @lc code=end

