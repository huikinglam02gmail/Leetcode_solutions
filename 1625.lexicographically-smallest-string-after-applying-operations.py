#
# @lc app=leetcode id=1625 lang=python3
#
# [1625] Lexicographically Smallest String After Applying Operations
#

# @lc code=start
from collections import deque


class Solution:
    # The key point is to note that the space of possible sequences is limited
    # 10 for digit * 100 for shift * 10 for addition
    # So just BFS the whole space and look for minimum
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        dq, visited = deque(), set()
        dq.append(s)
        visited.add(s)
        result = s
        while dq:
            node = dq.popleft()
            if node < result:
                result = node
            newNode1, newNode2 = '', ''
            for i, c in enumerate(node):
                if i % 2 == 1:
                    newNode1 += str((int(c) + a) % 10)
                else:
                    newNode1 += c
                newNode2 += node[(i + b) % len(s)]

            if newNode1 not in visited:
                dq.append(newNode1)
                visited.add(newNode1)
            if newNode2 not in visited:
                dq.append(newNode2)
                visited.add(newNode2)
        return result            

# @lc code=end

