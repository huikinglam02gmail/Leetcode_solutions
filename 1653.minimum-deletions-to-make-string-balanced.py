#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#

# @lc code=start
import bisect


class Solution:
    # Record the appearance of a and b at different indices
    # Then for each index, ask how many a I need to delete right of it + how many b I need to delete left of it
    # Take the minimum
    def minimumDeletionsBinarySearch(self, s: str) -> int:
        hashTable, n = {}, len(s)
        hashTable['a'] = []
        hashTable['b'] = []
        for i, c in enumerate(s):
            hashTable[c].append(i)
        
        result = n
        for i in range(n):
            result = min(result, bisect.bisect_right(hashTable['b'], i - 1) + len(hashTable['a']) - bisect.bisect_left(hashTable['a'], i + 1))
        return result

    # There is an O(n) way to do the problem
    # We practically need to find number of as and bs before and after each index
    def minimumDeletions(self, s: str) -> int:
        rightA, n = s.count('a'), len(s)
        leftB, result = 0, rightA
        for i in range(n):
            result = min(result, rightA + leftB)
            if s[i] == 'a':
                rightA -= 1
            else:
                leftB += 1
        return min(result, rightA + leftB)
            
# @lc code=end

