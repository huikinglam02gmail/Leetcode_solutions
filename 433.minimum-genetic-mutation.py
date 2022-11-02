#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque


class Solution:
    # BFS from start to end
    # Firstly, start and end must be able to mutate into a member in bank
    # Then we build up the graph of start + end + bank

    def canMutate(self, start, end):
        count = 0
        for c1, c2 in zip(start, end):
            if c1 != c2:
                count += 1
        return count <= 1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        count_start = 0
        for seq in bank:
            if self.canMutate(start, seq):
                count_start += 1
        if count_start == 0:
            return -1
        bank = set(bank)
        if end not in bank:
            return -1

        dq, visited, steps = deque(), set(), 0
        dq.append(start)
        visited.add(start)
        while dq:
            To_remove = set()
            for i in range(len(dq)):
                last = dq.popleft()
                if last == end:
                    return steps
                for nxt in bank:
                    if self.canMutate(last, nxt):
                        To_remove.add(nxt)
            for item in To_remove:
                dq.append(item)
                bank.remove(item)
            steps += 1
        return -1
# @lc code=end

