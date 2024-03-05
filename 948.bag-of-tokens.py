#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    To maximize score, we should do this:
    First sort the tokens
    With available power, get as many tokens from the small side until power is smaller than the front
    Then given up score to get more power, until either:
    1. There is only one entry and your power is lower than that
    2. There are no more entries
    We have sorted tokens, we can assure that if the queue has 2 entries
    (a, b) and power < a, getting b and losing a will not affect the score    
    '''
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens: return 0
        score, dq = 0, deque()
        tokens.sort()
        if power >= tokens[0]:
            for token in tokens: dq.append(token)
            while len(dq) > 1:
                if power >= dq[0]:
                    power -= dq.popleft()
                    score += 1
                else:
                    power += dq.pop()
                    score -= 1
            if power >= dq[0]: score += 1
        return score
# @lc code=end

