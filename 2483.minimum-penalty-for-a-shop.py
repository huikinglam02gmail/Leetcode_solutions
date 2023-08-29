#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#

# @lc code=start
class Solution:
    '''
    just do a scan. if the shop remains open for all n, the penalty is sum of appearance of N.
    Then if we close at i = n - 1, the penalty decreases by 1 if it is N, but increases by 1 if it is Y
    '''
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        result = n
        minimum = - customers.count('N')
        current = minimum
        for i in range(n - 1, -1, -1):
            if customers[i] == "N":
                current -= 1
            else:
                current += 1
            if current <= minimum:
                minimum = current
                result = i
        return result

# @lc code=end

