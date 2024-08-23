#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#

# @lc code=start
class Solution:
    def gcd(self, a, b):
        if a < b: a, b = b, a
        if b == 0: return a
        else: return self.gcd(b, a % b)

    def cleanUp(self, sign, prevNum, num, curNum, prevDenom):
        if sign: prevNum = prevNum * num + curNum * prevDenom
        else: prevNum = prevNum * num - curNum * prevDenom
        prevDenom *= num
        if prevNum < 0:
            factor = self.gcd(- prevNum, prevDenom)
            prevNum, prevDenom =  (- prevNum) // factor, prevDenom // factor
            prevNum = - prevNum
        else:
            factor = self.gcd(prevNum, prevDenom)
            prevNum, prevDenom =  (prevNum) // factor, prevDenom // factor
        return [prevNum, prevDenom]
        

    def fractionAddition(self, expression: str) -> str:
        prev_num = 0
        prev_denom = 1
        sign = True
        bottom = False
        num = 0
        cur_num = 0
        for i in range(len(expression)):
            if expression[i] in "-+":
                if bottom: prev_num, prev_denom = self.cleanUp(sign, prev_num, num, cur_num, prev_denom)                     
                sign = expression[i] == "+"
                num = 0
            elif expression[i] == "/":
                cur_num = num
                bottom = True
                num = 0
            else:
                num *= 10
                num += int(expression[i])
        
        prev_num, prev_denom = self.cleanUp(sign, prev_num, num, cur_num, prev_denom)
        return str(prev_num) + "/" + str(prev_denom)
# @lc code=end

