#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

class Solution:
    '''
    When k > 0, we always get a smaller number if current digit is smaller than the stack top.
    with each pop, k -= 1
    '''
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and stack[-1] > int(c) and k > 0:
                stack.pop()   
                k -= 1
            stack.append(int(c))
        while k > 0:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        else:
            i = 0
            while i < len(stack) and stack[i] == 0:
                i += 1
            if i == len(stack):
                return "0"
            else:
                string = ""
                for j in range(i, len(stack), 1):
                    string += str(stack[j])
                return string
# @lc code=end

