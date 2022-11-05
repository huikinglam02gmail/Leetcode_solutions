#
# @lc app=leetcode id=1434 lang=python3
#
# [1434] Number of Ways to Wear Different Hats to Each Other
#

# @lc code=start

class Solution:
    # There are less people than hat
    # So instead of assigning different hats to people
    # We should switch our viewpoint: we assign people to hat
    # mask = bitmask of whether the ith person has a hat on (does not matter which the person have)
    # dp(mask, h) = number of ways for people represented by mask is offered hat 1 to h
    # We are interested to know dp(1<<n-1, 40)
    # First we build a hat: person map
    # Base case: go through each person 0 to n-1
    # Sort the hats from small to large. 
    # From hat 0 to 39, add hat one by one
    # For each new hat, find who is wearable
    # For example, if j can wear the hat (i.e. j is inside hatToPeople[h])
    # We then find all the premask - postmask mapping in which the jth digit switch from 0 to 1
    # We can precompute this mapping in prePostSwitch
    # When each hat is allocated, we just accumulate the number of ways each mask can be reached
    def numberWays(self, hats: List[List[int]]) -> int:
        n, MOD, = len(hats), pow(10,9) + 7
        # Map from hat to wearable people
        hatToPeople = [[] for i in range(40)]
        for i, hatList in enumerate(hats):
            hatList.sort()
            for hat in hatList:
                hatToPeople[hat-1].append(i)

        prePostSwitch = [set() for i in range(n)]
        for i in range(1<<n):
            for j in range(n):
                if i & (1<<j) != 0:
                    prePostSwitch[j].add((i ^ (1<<j),i))

        dp = [0 for i in range(1<<n)]
        for h in range(40):
            dp_new = dp[:]
            for i in hatToPeople[h]:
                for pre, post in prePostSwitch[i]:
                    if pre == 0:
                        dp_new[post] += 1
                    else:
                        dp_new[post] += dp[pre]
                    dp_new[post] %= MOD
            dp = dp_new
        return dp[-1]
# @lc code=end

