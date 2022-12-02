#
# @lc app=leetcode id=1505 lang=python3
#
# [1505] Minimum Possible Integer After at Most K Adjacent Swaps On Digits
#

# @lc code=start
class Solution:
    # 1 <= k <= 109 -> raw BFS would not work
    # 1 <= num.length <= 3 * 104 -> if do it by bubble sort, it would amount to finding the smallest digit first seen smallest digit within the min(k, n) window
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k <= 0:
            return num
        elif k > n*(n-1) // 2:
            return ''.join(sorted([c for c in num]))
        else:
            i = 0
            while i < 10:
                index = num.find(str(i))
                if index >= 0 and index <= k:
                    return num[index] + self.minInteger(num[:index] + num[index+1:], k - index)
                else:
                    i += 1   
# @lc code=end

