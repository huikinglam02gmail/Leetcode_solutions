#
# @lc app=leetcode id=1449 lang=python3
#
# [1449] Form Largest Integer With Digits That Add up to Target
#

# @lc code=start
class Solution:
    # A knapsack problem
    # To get the maximum integer possible, For each possible cost, we get the rightmost one (largest digit)
    # dp(t) = largest possible integer with target t in string form
    # We should notice that the digits inside the string must be nonincreasing to achieve maximum
    # At each t, we pick from the available costs
    # Add to the string and sort
    # Compare with current answer
    def largerOfTwoIntegerStrings(self, s1, s2) -> str:
        if len(s1) > len(s2):
            return s1
        elif len(s2) > len(s1):
            return s2
        else:
            return max(s1, s2);

    def largestNumber(self, cost: List[int], target: int) -> str:
        Costs = {}
        for i, c in enumerate(cost):
            Costs[c] = i + 1
        dp = ["0"]*(target+1)
        for t in range(1, target + 1):
            for key in list(Costs.keys()):
                if t == key:
                    candidate = str(Costs[key])
                elif t > key and dp[t-key] != '0':
                    newCandidate = dp[t-key] + str(Costs[key])
                    newCandidate = sorted([*newCandidate], reverse=True)
                    candidate = ''.join(newCandidate)
                else:
                    candidate = '0'
                dp[t] = self.largerOfTwoIntegerStrings(dp[t], candidate)
        return dp[target]
# @lc code=end

