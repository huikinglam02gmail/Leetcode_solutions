#
# @lc app=leetcode id=1494 lang=python3
#
# [1494] Parallel Courses II
#

# @lc code=start
from collections import deque
from itertools import combinations
class Solution:
    # The number of courses n is limited: 1 <= n <= 15
    # Topological sorting would only tell you the sequence, but not necessarily the minimal semester count
    # And the state of courses can either be taken or not, bitmask DP would be more appropriate to solve the problem
    # use bitmask mask to denote whether course i + 1 is taken
    # We can BFS from mask = 0
    # When mask == 1 << n - 1, we finished all the courses and return steps (has to be correct by the shortest path property of BFS)
    # At each step, we check if a course is not yet taken (state & (1 << i) == 0) and prerequisite is obeyed (state & pre[i] == pre[i])
    # If so, we add the current course to candidate
    # We save dp[mask] as the shortest step to reach the mask state, and use for pruning unnecessary branches in future searches
    # If the length of candidate list l > k, we pick combinations of k out of l candidates
    # Otherwise we just study the whole candidate list in the current semester

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        dp = [n+1]*(1 << n)
        dp[0] = 0
        pre = [0]*n
        for before, after in relations:
            pre[after - 1] += (1 << (before - 1))
        dq = deque()
        dq.append([0, 0])
        while dq:
            mask, semester = dq.popleft()
            if mask == ((1 << n) - 1):
                return semester
            candidate = []
            for i in range(n):
                if (mask & (1 << i)) == 0 and (mask & pre[i]) == pre[i]:
                    candidate.append(i)
            if len(candidate) > k:
                candidates = list(combinations(candidate, k))
            else:
                candidates = [candidate]
            for candidate in candidates:
                newMask = mask
                for j in candidate:
                    newMask += (1 << j)
                if dp[newMask] > semester + 1:
                    dp[newMask] = semester + 1
                    dq.append([newMask, semester + 1])
# @lc code=end

