#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from typing import List


class Solution:
    '''
    Firstly, len(hand) % groupSize == 0
    Then build a hash table of occurence of different numbers. Then try to build the hands with keys from small to large      
    '''

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        hash_table = {}
        for card in hand: hash_table[card] = hash_table.get(card, 0) + 1
        keys = list(hash_table.keys())
        keys.sort()
        # start building
        i = 0
        while i < len(keys):
            if hash_table[keys[i]] == 0:
                i += 1
            elif hash_table[keys[i]] < 0:
                return False
            else:
                for j in range(groupSize):
                    if hash_table.get(keys[i] + j, 0) < 1: return False
                    else: hash_table[keys[i] + j] -= 1
        return True
# @lc code=end

