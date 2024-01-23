#
# @lc app=leetcode id=2578 lang=python3
#
# [2578] Split With Minimum Sum
#

# @lc code=start
class Solution:
    '''
    Sort the digits, add up odd and even digits
    '''
    def splitNum(self, num: int) -> int:
        arr = [int(c) for c in str(num)]
        arr.sort()
        newArr = [[], []]
        for i in range(len(arr)):
            newArr[i % 2].append(str(arr[i]))
        return int("".join(newArr[0])) + int("".join(newArr[1]))
        
# @lc code=end

