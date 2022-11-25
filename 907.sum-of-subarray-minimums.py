#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    # Another subarray problem that involves dp
    # A good strategy is to break it down into problems of subarrays that ends with index i (dp[i])
    # For example: [3,1,2,4] ->[3]; [3,1], [1]; [3,1,2],[1,2],[2]; [3,1,2,4],[1,2,4],[2,4],[4]
    # To get the sum, we have 3; 1 + 1; 1 + 1 + 2; 1 + 1 + 2 + 4
    # we should note that if arr[i] >= arr[i-1]; dp[i] = dp[i-1] + arr[i]
    # how about if arr[i] < arr[i-1] like 3,1 in the example?
    # Here comes a trick, we can add a 0 in front of 3. And then we maintain a monotonic increasing stack to hold the previous smallest number
    # Now we have [0,3,1,2,4]
    # 0: we have the stack as [0]
    # 1: 3: the stack will be [0,1], dp[1] = dp[0] + 3 = 3
    # 2: 1: we pop the 1 from the stack, and it becomes [0,2]. Because 1 is larger than 0, dp[2] = dp[0] + (2 - 0)*1 = 2 
    # 3: 2: the stack will be [0,2,3]. dp[3] = dp[2] + 2 = 4
    # 4: 2: the stack will be [0,2,3,4]. dp[4] = dp[3] + 4 = 8
    # Example 2:
    # arr = [0,11,81,94,43,3]
    # 0: stack = [0], dp[0] = 0
    # 1: stack = [0, 1], dp[1] = dp[0] + 11 = 11
    # 2: stack = [0, 1, 2], dp[2] = dp[1] + 81 = 92
    # 3: stack = [0, 1, 2, 3], dp[3] = dp[2] + 94 = 186
    # 4: stack = [0, 1, 4], dp[4] = dp[1] + (4-1)*43 = 140
    # 5: stack = [0, 5], dp[5] = dp[0] + (5-0)*3 = 15
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, dp = [], []
        arr = [0] + arr
        result, MOD = 0, pow(10,9)+7
        for i, num in enumerate(arr):
            if i == 0:
                dp.append(arr[i])
            else:
                while arr[stack[-1]] > num:
                    stack.pop()
                j = stack[-1]
                dp.append(dp[j] + (i-j)*num)
            stack.append(i)
            dp[i] %= MOD
            result += dp[i]
            result %= MOD
        return result
# @lc code=end

