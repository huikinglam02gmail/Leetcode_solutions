#
# @lc app=leetcode id=2019 lang=python3
#
# [2019] The Score of Students Solving Math Expression
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    0 <= answers[i] <= 1000
    This question is very similar to 312. Burst Balloons. Basically we don't really know which one we should do first, but we can break down into subproblems when we consider the possible output if an operator is executed last. 
    There is only 1 correct answer to get 5 points. For all the other possibilities we give 2 points
    '''
    @lru_cache(None)
    def dp(self, s):
        if '+' not in s and '*' not in s:
            return {int(s)}
        else:
            opIndices = []
            for i, c in enumerate(s):
                if c == '+' or c == '*':
                    opIndices.append(i)
            result = set()
            for i in opIndices:
                lSet = self.dp(s[:i])
                rSet = self.dp(s[i+1:])
                for l in lSet:
                    for r in rSet:
                        if s[i] == "+" and l + r <= 1000:
                            result.add(l + r)
                        if s[i] == "*" and l * r <= 1000:
                            result.add(l * r)
            return result

    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        possibleAnswers = {eval(s): 5}
        wrongAnswers = self.dp(s)
        for ans in wrongAnswers:
            if ans not in possibleAnswers:
                possibleAnswers[ans] = 2
        result = 0
        for ans in answers:
            result += possibleAnswers.get(ans, 0)
        return result
# @lc code=end

