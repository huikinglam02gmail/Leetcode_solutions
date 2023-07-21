#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Patience sort    
    put the numbers into decks
    paths holds the cumulative number of LIS as each new num is add onto the deck, so as I facilitate binary search
    check out the top of the decks, find if we can place num on top of each deck
    Requirement: num must be smaller than top of deck
    The top of the decks are always sorted
    We always use the leftmost deck
    if we see a number larger than some of the tops of the decks, we binary search the previous deck's path to look for number of LIS between the num and top of deck
    '''

    def findNumberOfLIS(self, nums: List[int]) -> int:
        decks, ends_decks, paths = [], [], []
        for num in nums:
            deck_idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if deck_idx > 0:
                l = bisect.bisect_right(decks[deck_idx - 1], -num)
                n_paths = paths[deck_idx - 1][-1] - paths[deck_idx - 1][l]
                
            if deck_idx == len(decks):
                decks.append([-num])
                ends_decks.append(num)
                paths.append([0,n_paths])
            else:
                decks[deck_idx].append(-num)
                ends_decks[deck_idx] = num
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])
        return paths[-1][-1]
# @lc code=end

