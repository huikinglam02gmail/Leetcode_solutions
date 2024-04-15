#
# @lc app=leetcode id=3095 lang=python3
#
# [3095] Shortest Subarray With OR at Least K I
#

# @lc code=start
from typing import List


class Solution:
    '''
    sliding window
    0 <= nums[i] <= 50: at most most 6 bits
    For each num in nums, we update current count of number of each bit. If removing the left element from the collecton would not make the subarray OR less than k, we would proceed to remove it.
    '''
    def updateHashTable(self, addOrRemove, num):
        for i in range(6):
            if num & (1 << i): 
                self.hashTable[i] = self.hashTable[i] + 1 if addOrRemove else self.hashTable[i] - 1
                if self.hashTable[i] == 1 and addOrRemove: self.current += (1 << i)
                if self.hashTable[i] == 0 and not addOrRemove: self.current -= (1 << i)

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left, n, self.current = 0, len(nums), 0
        self.hashTable = [0] * 6
        result = n + 1
        for right in range(n):
            self.updateHashTable(True, nums[right])
            if self.current >= k: result = min(result, right - left + 1)
            cannotProceed = False
            while left < right and not cannotProceed:
                self.updateHashTable(False, nums[left])
                if self.current >= k:
                    left += 1
                    result = min(result, right - left + 1)
                else:
                    cannotProceed = True
                    self.updateHashTable(True, nums[left])
        return result if result <= n else -1
           
# @lc code=end

