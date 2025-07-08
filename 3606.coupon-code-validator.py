#
# @lc app=leetcode id=3606 lang=python3
#
# [3606] Coupon Code Validator
#

# @lc code=start
from typing import List


class Solution:
    def validator(self, code):
        for c in code:
            if not c.isalpha() and not c.isdigit() and c != '_':
                return False
        return True

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result = [[] for i in range(4)]
        for i in range(len(code)):
            if isActive[i] and len(code[i]) > 0 and self.validator(code[i]):
                if businessLine[i] == "electronics":
                    result[0].append(code[i])
                elif businessLine[i] == "grocery":
                    result[1].append(code[i])
                elif businessLine[i] == "pharmacy":
                    result[2].append(code[i])
                elif businessLine[i] == "restaurant":
                    result[3].append(code[i])
        
        for i in range(4): result[i].sort()
        return result[0] + result[1] + result[2] + result[3]
# @lc code=end

