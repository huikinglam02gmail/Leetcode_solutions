#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= words.length <= 14
    We can use bitmask + DP to solve the problem
    However, the order of addition does not matter, it is always limited by the quantity of letters given
    Therefore we can iterate through the bitmask from 1 to 2^n-1
    Each time we just ask if bitmask can be formed from bitmask^(1 << first significant digit)
    To avoid repeated calculation, we can store both the max score and corresponding available letters in the hash table    
    '''    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        dp = [[-1] for i in range(pow(2,n))]
        letter_counter = [0]*26
        for letter in letters: letter_counter[ord(letter) - ord('a')] += 1
        dp[0][0] = 0
        dp[0].append(letter_counter)
        result = 0
        
        for mask in range(1, pow(2,n)):
            bl = mask.bit_length()
            prev_mask = mask^(1 << (bl-1))
            if dp[prev_mask][0] >= 0:
                cur_letters = [0]*26
                cur_score = 0
                for c in words[bl-1]:
                    cur_letters[ord(c)-ord('a')] += 1
                    cur_score += score[ord(c)-ord('a')]
                can_use = all([cur_letters[i] <= dp[prev_mask][1][i] for i in range(26)])
                if can_use:
                    dp[mask][0] = dp[prev_mask][0] + cur_score
                    result = max(result, dp[mask][0])
                    dp[mask].append([dp[prev_mask][1][i] - cur_letters[i] for i in range(26)])        
        return result
                    # @lc code=end

