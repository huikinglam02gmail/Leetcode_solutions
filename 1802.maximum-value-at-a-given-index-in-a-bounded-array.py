#
# @lc app=leetcode id=1802 lang=python3
#
# [1802] Maximum Value at a Given Index in a Bounded Array
#

# @lc code=start
class Solution:
    '''
    1 <= n <= maxSum <= 10^9 -> don't try to generate the array!
    Instead, guess the answer by binary search. set nums[index] = k. The minimum sum possible while obeying the given condition is [..., k - 1, k, k-1, ...]
    on the left, the first index which is 1 is index - k + 1
    on the right, the first index which is 1 is index + k - 1
    Mathematically we have left and right sum if both side add down to 1 = k + (k - 1) * k = k^2
    So on the left, contribution by 1 is max(0, index - k + 1)
    on the right, contribution by 1 is max(0, n - index - k)
    If index - k + 1 < 0, at array[0] we have k - index. minus (k - index - 1) * (k - index) // 2 to the sum
    if index + k - 1 >= n, at array[n - 1] we have k - (n - 1 - index) minus (k - (n - index)) * (k - n + index + 1) // 2 from the sum
    I used the bisectRight algorithm to make sure the binary search
    '''
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = 0, maxSum + 1
        while l < r:
            k = l + (r - l) // 2
            S = k * k
            S += max(0, index - k + 1)
            S += max(0, n - index - k)
            if index - k + 1 < 0:
                S -= (k - index - 1) * (k - index) // 2
            if index + k - 1 >= n:
                S -= (k - (n - index)) * (k - n + index + 1) // 2
            if S <= maxSum:
                l = k + 1
            else:
                r = k
        return l - 1
# @lc code=end
