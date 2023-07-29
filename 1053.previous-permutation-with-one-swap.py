#
# @lc app=leetcode id=1053 lang=python3
#
# [1053] Previous Permutation With One Swap
#

# @lc code=start
from typing import List


class Solution:
    '''
    To find previous permutation (with one swap), follow this algorithm:
    Find largest index i such that arr[i] > arr[i+1], for 0 <= i < n-1
    if the i found is -1: return arr
    Find largest index j such that j > i and arr[j] < arr[i].
    Swap arr[i] and arr[j]
    return arr    
    '''

    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n-2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        if i >= 0:
            j = n-1
            while j > i and arr[i] <= arr[j]:
                j -= 1
            while j > 0 and arr[j-1] == arr[j]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        return arr
# @lc code=end

