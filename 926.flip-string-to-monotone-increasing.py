#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    # This is a DP problem
    # Just imagine we have already ordered s[:i] with "flips" flips
    # It could end with either 0 or 1
    # Now we have s[i] coming in, it can be 1 or 0
    # if it is 1, it always works to append to s[:i]
    # On the other hand, if it is 0, we can do 2 things:
    # 1. flip 0 to 1. then flips += 1
    # 2. Keep the current to be 0 and flip all ones before to be 0
    # To account for the second state, we can keep counting number of ones occurred
    # then flips = min(flips + 1, counter)
    def minFlipsMonoIncr(self, s: str) -> int:
        counter, flips = 0, 0
        for c in s:
            if c == "1":
                counter += 1
            else:
                flips = min(flips+1, counter)
        return flips
        
# @lc code=end

