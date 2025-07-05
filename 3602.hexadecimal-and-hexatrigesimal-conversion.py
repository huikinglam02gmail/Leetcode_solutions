#
# @lc app=leetcode id=3602 lang=python3
#
# [3602] Hexadecimal and Hexatrigesimal Conversion
#

# @lc code=start
class Solution:
    def concatHex36(self, n: int) -> str:
        hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        hexatrigesimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        dec = ""
        triges = ""
        n1 = pow(n, 2)
        while n1 > 0:
            dec = hexadecimal[n1 % 16] + dec
            n1 //= 16
        n1 = pow(n, 3)
        while n1 > 0:
            triges = hexatrigesimal[n1 % 36] + triges
            n1 //= 36
        return dec + triges
# @lc code=end

