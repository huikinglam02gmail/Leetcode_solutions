#
# @lc app=leetcode id=2937 lang=python3
#
# [2937] Make Three Strings Equal
#

# @lc code=start
class Solution:
    '''
    Find the longest common prefix string among the 3
    '''
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lengthOrder = [s1, s2, s3]
        lengthOrder.sort(key = lambda x: len(x))
        i = len(lengthOrder[0])
        while i > 0 and (not lengthOrder[1].startswith(lengthOrder[0][:i]) or not lengthOrder[2].startswith(lengthOrder[0][:i])) :
            i -= 1
        if i == 0: return -1
        else: return sum([len(x) - i for x in lengthOrder])
# @lc code=end

