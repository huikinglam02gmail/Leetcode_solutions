#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    # To be gcd, we look for factors that divides both len(str1) and len(str2)
    # Then we just test if str1 and str2 is repeat of the the specified substring
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        start = min(l1, l2)
        
        for i in range(start, 0, -1):
            if l1 % i == 0 and l2 % i == 0:
                j1, j2 = 0, 0
                string = str1[j1 : j1 + i]
                while j1 <= l1 - i and str1[j1 : j1 + i] == string:
                    j1 += i
                while j2 <= l2 - i and str2[j2 : j2 + i] == string:
                    j2 += i
                if j1 == l1 and j2 == l2:
                    return string
        return ""
# @lc code=end

