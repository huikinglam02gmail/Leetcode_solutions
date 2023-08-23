#
# @lc app=leetcode id=1865 lang=python3
#
# [1865] Finding Pairs With a Certain Sum
#

# @lc code=start
from typing import List


class FindSumPairs:
    '''
    1 <= nums1.length <= 1000
    1 <= nums2.length <= 10^5
    At most 1000 calls are made to add and count each.
    nums1 is much shorter than nums2 and all add will be to nums2
    So, keep a counter dictionary of nums2
    for each add, we update nums2: nums2[index] += val, and update the hashTable
    for each count call, sum up count[tot - nums1[i]]
    '''
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.hashTable = {}
        self.nums1 = nums1
        self.nums2 = nums2
        for num in self.nums2:
            self.hashTable[num] = self.hashTable.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        self.hashTable[self.nums2[index]] -= 1
        self.hashTable[self.nums2[index] + val] = self.hashTable.get(self.nums2[index] + val, 0) + 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1:
            result += self.hashTable.get(tot - num, 0)
        return result


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end

