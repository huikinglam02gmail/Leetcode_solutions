#
# @lc app=leetcode id=1801 lang=python3
#
# [1801] Number of Orders in the Backlog
#

# @lc code=start
class Solution:
    '''
    Typical priority queue question. Just simulate what will happen
    '''
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        transactions = [[], []]
        MOD = pow(10, 9) + 7
        for p, a, o in orders:
            while transactions[1 - o] and transactions[1 - o][0][0] <= p * pow(-1, o) and a > 0:
                p1, a1 = heapq.heappop(transactions[1 - o])
                deduct = min(a1, a)
                a1 -= deduct
                a -= deduct
                if a1 > 0:
                    heapq.heappush(transactions[1 - o], [p1, a1])
            if a > 0:
                heapq.heappush(transactions[o], [pow(-1, 1 - o) * p, a])
        return sum([sum([ a for p, a in heap]) for heap in transactions]) % MOD               
        
# @lc code=end
