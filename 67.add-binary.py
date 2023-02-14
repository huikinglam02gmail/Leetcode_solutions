#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    # Always impose len(a) >= len(b)
    # Then add from the back
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            return self.addBinary(b, a)
        result = []
        na, nb, carry = len(a), len(b), 0
        for i in range(na - 1, -1, -1):
            if i >= na - nb:
                carry, ans = divmod(int(a[i]) + int(b[i - na + nb]) + carry, 2)
            else:
                carry, ans =  divmod(int(a[i]) + carry, 2)
            result.append(str(ans))
        if carry > 0:
            result.append('1')
        return "".join(result[::-1])
            

# @lc code=end

