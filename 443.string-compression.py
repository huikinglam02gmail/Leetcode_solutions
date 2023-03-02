#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
from typing import List


class Solution:
    '''
    Need to modify chars in place
    '''
    def compress(self, chars: List[str]) -> int:        
        left, right, n, result = 0, 0, len(chars), 0
        while right < n:
            result += 1
            chars[left], count = chars[right], 0
            while right < n and chars[right] == chars[left]:
                right += 1
                count += 1
            left += 1
            if count > 1:
                lastLeft, diff = left, str(count)
                while left - lastLeft < len(diff):
                    result += 1
                    chars[left] = diff[left - lastLeft]
                    left += 1
        return result

        
# @lc code=end

