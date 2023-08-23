#
# @lc app=leetcode id=1864 lang=python3
#
# [1864] Minimum Number of Swaps to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    '''
    First think about when is impossible:
    if len(s) % 2 == 0 and count('0') != count('1')
    if len(s) $ 2 == 1 and abs(count('0') - count('1')) > 1
    else
    We just find out if the cost to min Cost to get the string to become s[even] = 1 or 0
    '''
    def minSwaps(self, s: str) -> int:
        count0 = 0
        for i, c in enumerate(s):
            if c == '0':
                count0 += 1
        n = len(s)
        if abs(2 * count0 - n) > (n % 2):
            return -1
        else:
            zeroInWrongPlace = [0, 0]
            if count0 == n - count0 - 1:
                zeroInWrongPlace[0] = float("inf")
            if count0 == n - count0 + 1:
                zeroInWrongPlace[1] = float("inf")
            for i in range(n):
                if s[i] == '0':
                    if i % 2 == 0:
                        zeroInWrongPlace[1] += 1
                    else:
                        zeroInWrongPlace[0] += 1
            return min(zeroInWrongPlace)
# @lc code=end

