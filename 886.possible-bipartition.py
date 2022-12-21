#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph =  [[] for i in range(n)]
        for dislike in dislikes:
            graph[dislike[0]-1].append(dislike[1]-1)
            graph[dislike[1]-1].append(dislike[0]-1)
            
        set_0, set_1 = set(), set()
        for i in range(n):
            if i not in set_0 and i not in set_1:
                dq = deque()
                dq.append(i)                
                set_0.add(i)
                while dq:
                    node = dq.popleft()
                    for j in graph[node]:
                        if node in set_0:
                            if j in set_0:
                                return False
                            if j not in set_1:
                                set_1.add(j)
                                dq.append(j)
                        if node in set_1:
                            if j in set_1:
                                return False
                            if j not in set_0:
                                set_0.add(j)
                                dq.append(j)
        return True
             
# @lc code=end

