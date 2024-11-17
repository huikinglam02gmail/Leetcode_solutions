#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Precompute prefix sum
    [2, -1, 2] -> [0, 2, 1, 3], k = 3
    We will use a monotonic increasing queue to solve the problem
    The key idea is this:
    We maintain a monotonically increasing queue to store the possible starting point of subarray
    a dry run:
    [0]: 2 - 0 < k = 3, we just append the 2 to the right: [0, 2]
    for the 1, first 1 - 0 < k. And 1 is smaller than 2, so we pop out the 2, and push the 1 in
    The 2 is not used anymore because firstly, any future subarray that starts with 1 will be shorter than of 2
    Also, as 1 is smaller, it has better chance of hitting at sum >=k
    When the 3 comes in 3 - 0 = 3 = k. We then pop the 0 and it will not be used any more. That's because the any future numbers that uses this 0 will be longer than 3.
    we further compare with the 1 and find it is below k. so append to the right: [1,3]    
    '''
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixes = [0]
        for num in nums: prefixes.append(prefixes[-1] + num)
        
        dq = deque()
        result = len(prefixes)
        for i, prefix in enumerate(prefixes):
            while dq and prefix - prefixes[dq[0]] >= k: result = min(result, i - dq.popleft())
            while dq and prefix < prefixes[dq[-1]]: dq.pop()
            dq.append(i)
        return -1 if result == len(prefixes) else result
            
# @lc code=end

