#
# @lc app=leetcode id=1477 lang=python3
#
# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
#

# @lc code=start
import bisect
from typing import List

class Solution:
    # left[i] = minimum length of subarrays within arr[:i] that sum up to target
    # right[i] = minimum length of subarrays within arr[i:] that sum up to target    
    # As 1 <= arr[i] <= 1000, the prefix sum array is strictly increasing
    # Prepare the prefix sum array
    # Scan from left to right:
    # left[i] = min(left[i-1], binary searched index in which prefix[j] = prefix[i+1] - target)
    # right[i] = min(right[i+1], binary searched index in which prefix[j] = prefix[i+1] + target)
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        n = len(arr)
        left = [float('Inf') for i in range(n)]
        right = [float('Inf') for i in range(n)]
        for i in range(1, n):
            left[i] = left[i-1]
            index = bisect.bisect_left(prefix, prefix[i] - target)
            if prefix[index] == prefix[i] - target:
                left[i] = min(left[i], i - index)
        for i in range(n-1,-1,-1):
            if i == n-1:
                if arr[i] == target:
                    right[i] = 1
            else:
                right[i] = right[i+1]
                index = bisect.bisect_left(prefix, prefix[i] + target)
                if index < n +1 and prefix[index] == prefix[i] + target:
                    right[i] = min(right[i], index-i)
        result = float('Inf')
        for i in range(1,n-1):
            result = min(result, left[i] + right[i])
        if result < float('Inf'):
            return result
        else:
            return -1

#sol = Solution()
#ans = sol.minSumOfLengths([64,5,20,9,1,39],69)
#print(ans)
# @lc code=end

