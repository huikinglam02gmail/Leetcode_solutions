#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#

# @lc code=start
from typing import List


class Solution:
    '''
    A DP problem  
    dp[i] = minimum possible height that the total bookshelf can be after placing books[:i+1]
    Minimum possible height to place i books can be achieved by searching for previous rows to incorporate
    Recurrence relation: dp[i] = dp[j] + max(books[j + 1:i + 1][1])
    where sum(books[j+1:i+1][0]) < shelfWidth    
    '''
    
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0 for i in range(n)]
        dp[0] = books[0][1]
        for i in range(1, n):
            dp[i] = books[i][1] + dp[i - 1]
            j, total_thickness, max_height = i, 0, 0
            while j >= 0 and total_thickness <= shelfWidth:
                total_thickness += books[j][0]
                max_height = max(max_height, books[j][1])
                j -= 1
                if total_thickness <= shelfWidth:
                    if j >= 0: dp[i] = min(dp[i], dp[j] + max_height)
                    else: dp[i] = min(dp[i], max_height)
        return dp[-1]
# @lc code=end

