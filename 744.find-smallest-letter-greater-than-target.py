#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Binary search    
    '''
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect_right(letters, target)
        return letters[i % len(letters)]
# @lc code=end

