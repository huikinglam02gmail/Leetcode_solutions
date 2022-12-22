#
# @lc app=leetcode id=1562 lang=python3
#
# [1562] Find Latest Group of Size M
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList

class Solution:
    # At the end it's all 1
    # We could simulate from the end and backtrack:
    # At i = n-1, the string has n 1s
    # Then at each step, we binary search for the interval to break
    # and modify the interval
    # In addition, we can keep a length to interval map
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if len(arr) == 1:
            return 1
        elif n == m:
            return n
        lengthToInterval = {}
        intervalToLength = {}
        intervalEnds = SortedList()
        

        lengthToInterval[n] = set()
        lengthToInterval[n].add(n)
        intervalToLength[n] = n
        intervalEnds.add(n)
        
        for i in range(n-1, -1 ,-1):
            ind = intervalEnds.bisect_left(arr[i])
            lengthOfInterval = intervalToLength[intervalEnds[ind]]
            start, end = intervalEnds[ind] - lengthOfInterval + 1, intervalEnds[ind]
            leftLength, rightLength = arr[i] - start, end - arr[i]
            intervalToLength.pop(end)
            lengthToInterval[lengthOfInterval].remove(end)
            intervalEnds.pop(ind)

            if leftLength > 0:
                intervalToLength[arr[i]-1] = leftLength
                if leftLength not in lengthToInterval:
                    if leftLength == m:
                        return i
                    else:
                        lengthToInterval[leftLength] = set()
                lengthToInterval[leftLength].add(arr[i]-1)
                intervalEnds.add(arr[i]-1)
            if rightLength > 0:
                intervalToLength[end] = rightLength
                if rightLength not in lengthToInterval:
                    if rightLength == m:
                        return i
                    else:
                        lengthToInterval[rightLength] = set()
                lengthToInterval[rightLength].add(end)
                intervalEnds.add(end)
        return -1

# @lc code=end
