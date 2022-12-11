#
# @lc app=leetcode id=1520 lang=python3
#
# [1520] Maximum Number of Non-Overlapping Substrings
#

# @lc code=start
from typing import List
import bisect


class Solution:
    # ok substrings must start from where a character is first seen
    # The shortest possible ok substring ends with the same character last seen, if and only if all the rest characters either is totally inside the current range or completely outside
    # If we see partial overlap, we change the end to that of the overlapping character, and test again
    # Once we arrive at an ok substring, we save the start and end, and sort by the end
    # Then try to build an nonoverlapping sequence from the sorted list. Throw away intervals with start smaller than current end
    # To make a substring valid, characters must either
    # 1. never appear inside the range => if we search the current start and end inside the appearance list, they must have the same index
    # 2. 
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        appear, n = {}, len(s)
        for i in range(n):
            if s[i] not in appear:
                appear[s[i]] = []
            appear[s[i]].append(i)
        keys = list(appear.keys())
        candidates = []
        for key1 in keys:
            start, end = appear[key1][0], appear[key1][-1]
            foundSubstring, impossible = False, False
            while not impossible and not foundSubstring:
                count = 0
                for key2 in keys:
                    indStart = bisect.bisect_left(appear[key2], start)
                    indEnd = bisect.bisect_right(appear[key2], end)
                    if indStart != indEnd and appear[key2][0] < start:
                        impossible = True
                        break
                    elif indStart != indEnd and appear[key2][-1] > end:
                        end = appear[key2][-1]
                        break
                    else:
                        count += 1
                if count == len(keys):
                    foundSubstring = True
            if not impossible and foundSubstring:
                candidates.append([end, start])
        candidates.sort()
        lastEnd = -1
        result = []
        for end, start in candidates:
            if start > lastEnd:
                result.append(s[start:end+1])
                lastEnd = end
        return result
# @lc code=end

