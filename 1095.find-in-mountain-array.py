#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    '''
    Firstly figure out the length of the whole array (1 call)
    Then figure out where is the peak by check local neighbourhood (3logN calls)
    Reuse code from Leetcode 852. Peak Index in a Mountain Array
    Then binary search for target on both sides of the peak
    return the lesser one if there are two    
    '''
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            A = [mountain_arr.get(mid - 1), mountain_arr.get(mid),  mountain_arr.get(mid + 1)]
            if A[0] < A[1] > A[2]:
                break
            elif A[0] < A[1] < A[2]:
                left = mid
            else:
                right = mid
        left, right = 0, mid + 1
        while left < right:
            mid = left + (right - left) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num <target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= 0 and mountain_arr.get(left) == target:
            return left
        left, right = mid, n
        while left < right:
            mid = left + (right - left) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                left = mid + 1
            else:
                right = mid - 1
        if left < n and mountain_arr.get(left) == target:
            return left
        return -1
# @lc code=end

