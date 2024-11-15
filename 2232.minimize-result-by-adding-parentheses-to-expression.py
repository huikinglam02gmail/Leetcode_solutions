#
# @lc app=leetcode id=2232 lang=python3
#
# [2232] Minimize Result by Adding Parentheses to Expression
#

# @lc code=start
class Solution:
    def evaluate(self, expression):
        nums = [1, 1, 1, 1]
        expressionSplit = expression.split('+')
        if expressionSplit[0].find('(') == 0: nums[1] = int(expressionSplit[0][1:])
        else:
            nums[0], nums[1] = [int(x) for x in expressionSplit[0].split('(')]
        if expressionSplit[1].find(')') == len(expressionSplit[1]) - 1: nums[2] = int(expressionSplit[1][:-1])
        else:
            nums[2], nums[3] = [int(x) for x in expressionSplit[1].split(')')]
        return nums[0] * (nums[1] + nums[2]) * nums[3]

    def minimizeResult(self, expression: str) -> str:
        ind = expression.find('+')
        minSoFar = float("inf")
        result = ""
        for i in range(ind):
            for j in range(ind + 2, len(expression) + 1):
                current = self.evaluate(expression[:i] + '(' + expression[i:ind] + '+' + expression[ind + 1:j] + ')' + expression[j:])
                if minSoFar > current:
                    minSoFar = current
                    result = expression[:i] + '(' + expression[i:ind] + '+' + expression[ind + 1:j] + ')' + expression[j:]
        return result
# @lc code=end

