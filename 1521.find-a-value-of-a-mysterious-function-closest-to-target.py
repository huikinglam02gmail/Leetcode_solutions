#
# @lc app=leetcode id=1521 lang=python3
#
# [1521] Find a Value of a Mysterious Function Closest to Target
#

# @lc code=start
class Solution:
    # subarray AND decreases with length
    # So we can iterate from the back
    # subarray & starting from arr[i] = arr[i] union arr[i] & set of subarry & starting from arr[i+1]
    def closestToTarget(self, arr: List[int], target: int) -> int:
        result = float('inf')
        n = len(arr)
        hashSet = set()
        for i in range(n-1, -1, -1):
            hashSetNew = set()
            hashSetNew.add(arr[i])
            result = min(result, abs(arr[i] - target))
            for j in hashSet:
                hashSetNew.add(arr[i]&j)
                result = min(result, abs((arr[i]&j) - target))
            hashSet = hashSetNew.copy()            
        return result
# @lc code=end

