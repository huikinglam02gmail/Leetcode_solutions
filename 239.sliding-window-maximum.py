#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
from typing import List

class MonotonicDecreasingQueue:
    '''
    A monotonic decreasing queue hold the value at the first index and the index at the second index
    '''
    def __init__(self, nums) -> None:
        self.queue = deque()
        data = [[v, i] for i, v in enumerate(nums)]
        for v, i in data:
            self.insert(v, i)
    
    def insert(self, value, index):
        while self.queue and value > self.queue[-1][0]:
            self.queue.pop()
        self.queue.append([value, index])


class Solution:
    '''
    Maintain a monotonic decreasing dequeue. When a new number comes in, we first check if the front of the queue is already out of range. If so, just toss it
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        MDQ = MonotonicDecreasingQueue(nums[:k])
        result = []
        result.append(MDQ.queue[0][0])
        for i in range(k, len(nums)):
            if i == k + MDQ.queue[0][1]:
                MDQ.queue.popleft()
            MDQ.insert(nums[i], i)
            result.append(MDQ.queue[0][0])
        return result
# @lc code=end

