#
# @lc app=leetcode id=1601 lang=python3
#
# [1601] Maximum Number of Achievable Transfer Requests
#

# @lc code=start
class Solution:
    # 1 <= n <= 20
    # 1 <= requests.length <= 16
    # We can simply backtrack
    # Find out if the final state occupancy is the same as initial, given different masks

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        result = 0
        m = len(requests)
        for mask in range(1 << m):
            flow = [0]*n
            count = 0
            for j in range(m):
                if mask & (1 << j) != 0:
                    flow[requests[j][0]] -= 1
                    flow[requests[j][1]] += 1
                    count += 1
            if all([x == 0 for x in flow]):
                result = max(result, count)
        return result
# @lc code=end

