#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#

# @lc code=start
class Solution:
    '''
    result: digit to test first
    k: decrease one so that 0 is not included
    approach: count how many lexicographically sorted numbers are there starting with result.
    For example, Before considering numbers starting with 2, we first consider 10, 11, ..., 19
    interval refers to the current interval under consideration
    over count is avoided by taking the min(n + 1) with interval end (to count 0 as well)
    Decision to investigate:
    if k is larger than count of numbers starting with the current digit, move on to the next digit and chop off k
    if not, the remaining numbers must start with current digit. Upscale result by power of ten and keep comparing k and count    
    '''
    def findKthNumber(self, n: int, k: int) -> int:
        result = 1
        k -= 1
        while k > 0:
            count = 0
            interval = [result, result + 1]
            while interval[0] <= n:
                count += (min(n + 1, interval[1]) - interval[0])
                interval = [10 * interval[0], 10 * interval[1]]
            
            if k >= count:
                result += 1
                k -= count
            else:
                result *= 10
                k -= 1
        return result
# @lc code=end

