#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    First we sort deck
    Because 1 <= deck.length <= 1000, this is not crazy large input, we can simulate the process
    One way to it efficiently is to use a deque(), because we do not really to operate on nodes in the middle of the queue.
    The way to go is keep a queue with node value index 0 : len(deck) - 1
    In each operation, we first popleft one node and assign the smallest unused deck number to the index specified by the node
    We popleft the second time and append back to the queue    
    '''
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n, j = len(deck), 0
        result, dq = [0] * n, deque()
        deck.sort()
        for i in range(n):
            dq.append(i)
        while len(dq) >= 2:
            result[dq.popleft()] = deck[j]
            j += 1
            dq.append(dq.popleft())
        result[dq.popleft()] = deck[j]
        return result
# @lc code=end

