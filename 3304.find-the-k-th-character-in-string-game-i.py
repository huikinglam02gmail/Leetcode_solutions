#
# @lc app=leetcode id=3304 lang=python3
#
# [3304] Find the K-th Character in String Game I
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        arr = ['a']
        while len(arr) < k:
            arr = arr + [chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in arr]
        return arr[k - 1]
# @lc code=end

