#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    '''
    1 <= n <= 100
    1 <= k <= n
    We search for sliding windows of size k, maximum count of "B"
    return k - count    
    '''
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n, max_seen, BCount = len(blocks), 0, 0
        for i in range(n):
            if i >= k and blocks[i - k] == "B": BCount -= 1
            if blocks[i] == "B": BCount += 1
            max_seen = max(max_seen, BCount)
        return k - max_seen
# @lc code=end

