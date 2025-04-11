#
# @lc app=leetcode id=2999 lang=python3
#
# [2999] Count the Number of Powerful Integers
#

# @lc code=start
class Solution:
    '''
    Simplify the question: if we can find the total number of powerful integers smaller than or equal to x, the answer is ans[finish] - ans[start - 1]
    Then for x, there are 3 scenarios:
    1. len(x) < len(s): 0
    2. len(x) == len(s): 1 if x >= s else 0
    3. len(x) > len(s): for each digit in the prefix 0 <= i < len(x) - len(s), compare x[i] and limit:
        a. if x[i] > limit: there can be (limit + 1) ^ (len(x) - len(s) - i) possibilities after it. Stop trying smaller numbers
        b. there can be x[i] * (limit + 1) ^ (len(x) - len(s) - i - 1) possibiltiies. add 1 if the suffix is larger than s
    '''
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return self.powerfulIntegers(str(finish), s, limit) - self.powerfulIntegers(str(start - 1), s, limit)
    
    def powerfulIntegers(self, x, s, limit):
        if len(x) < len(s): return 0
        result = 0
        for i in range(len(x) - len(s)): 
            if int(x[i]) > limit:
                result += pow(limit + 1, len(x) - len(s) - i)
                return result
            else:
                result += int(x[i]) * pow(limit + 1, len(x) - len(s) - i - 1)
        if x[len(x) - len(s):] >= s: result += 1
        return result
# @lc code=end
