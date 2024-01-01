#
# @lc app=leetcode id=2049 lang=python3
#
# [2049] Count Nodes With the Highest Score
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    We want to record the size of subtree under a node. It's 1 + size(subtree1) + size(subtree2)
    Now if we remove a node with both children and parent, the size(children1) * size(children2) * (n - size(node))
    '''
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [set() for i in range(n)]
        offsprings = [0] * n
        for i, p in enumerate(parents):
            if p >= 0:
                children[p].add(i)
                offsprings[p] += 1
        subtreeSize = [1] * n
        dq = deque()
        for i, offspring in enumerate(offsprings):
            if offspring == 0: dq.append(i)
        while dq:
            node = dq.popleft()
            if parents[node] >= 0:
                offsprings[parents[node]] -= 1
                subtreeSize[parents[node]] += subtreeSize[node]
                if offsprings[parents[node]] == 0: dq.append(parents[node])
        counts = {}
        for i in range(n):
            score = 1
            for child in children[i]:
                score *= subtreeSize[child]
            if parents[i] >= 0: score *= n - subtreeSize[i]
            counts[score] = counts.get(score, 0) + 1
        return counts[max(counts.keys())]

# @lc code=end

