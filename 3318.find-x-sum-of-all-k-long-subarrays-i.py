#
# @lc app=leetcode id=3318 lang=python3
#
# [3318] Find X-Sum of All K-Long Subarrays I
#

# @lc code=start
from typing import List


class Solution:
    '''
    We keep two sorted lists, one keeping the top x most frequent elements and the second keeping the rest
    Also keep track of occurrence of all the elements in a hash table
    '''
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        occur = {}
        self.top = SortedList()
        self.bottom = SortedList()
        result = []
        self.S = 0
        for i in range(len(nums)):
            if i >= k:
                fromTop = False
                if [occur[nums[i - k]], nums[i - k]] in self.top: 
                    self.top.remove([occur[nums[i - k]], nums[i - k]])
                    self.S -= occur[nums[i - k]] * nums[i - k]
                    fromTop = True
                else: 
                    self.bottom.remove([occur[nums[i - k]], nums[i - k]])
                occur[nums[i - k]] -= 1
                if occur[nums[i - k]] == 0: occur.pop(nums[i - k])
                elif not fromTop: 
                    self.top.add([occur[nums[i - k]], nums[i - k]])
                    self.S += occur[nums[i - k]] * nums[i - k]
                else:
                    self.bottom.add([occur[nums[i - k]], nums[i - k]])
            self.balance(x)
            fromTop = False                                   
            if nums[i] not in occur: occur[nums[i]] = 0
            elif [occur[nums[i]], nums[i]] in self.top:
                self.top.remove([occur[nums[i]], nums[i]])
                self.S -= occur[nums[i]] * nums[i]
                fromTop = True
            else:
                self.bottom.remove([occur[nums[i]], nums[i]])
            occur[nums[i]] += 1
            if not fromTop:
                self.top.add([occur[nums[i]], nums[i]])
                self.S += occur[nums[i]] * nums[i]
            else:
                self.bottom.add([occur[nums[i]], nums[i]])
            self.balance(x)
            if i >= k - 1: result.append(self.S)
        return result
    
    def balance(self, x):
        while len(self.top) > x:
            freq, num = self.top.pop(0)
            self.S -= freq * num
            self.bottom.add([freq, num])
        while len(self.top) < x and len(self.bottom) > 0:
            freq, num = self.bottom.pop(-1)
            self.S += freq * num
            self.top.add([freq, num])

# @lc code=end

