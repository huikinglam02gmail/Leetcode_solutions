#
# @lc app=leetcode id=1782 lang=python3
#
# [1782] Count Pairs Of Nodes
#

# @lc code=start
from typing import List


class Solution:
    '''
    If we just consider the edges upfront, we will have a hard time counting pairs since 2 <= n <= 2 * 10^4. On the other hand, if we change the question, if count[i] = number of edges connected to node i, by sorting count[:], we can easily find the number of pairs (i,j) (in the sorted array) in which i < j and count[i] + count[j] > q (a two sum problem).
    Then among these pairs, so of them are not qualified because count[i] + count[j] and count[i] + count[j] - # appearance of edge <= q. So just deduct the two to get the answer. 
    '''
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        count = [0] * n
        edgeCount = {}
        for a, b in edges:
            count[a - 1] += 1
            count[b - 1] += 1
            pair = (min(a - 1, b - 1), max(a - 1, b - 1))
            edgeCount[pair] = edgeCount.get(pair, 0) + 1
        
        sortedCount = sorted(count)
        result = []
        for q in queries:
            l, r = 0, n - 1
            res = 0
            while l < r:
                if sortedCount[l] + sortedCount[r] <= q:
                    l += 1
                else:
                    res += r - l
                    r -= 1
            for t, b in edgeCount.items():
                if count[t[0]] + count[t[1]] > q and count[t[0]] + count[t[1]] - b <= q:
                    res -= 1
            result.append(res)
        return result        
# @lc code=end

