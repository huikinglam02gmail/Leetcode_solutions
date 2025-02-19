#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#

# @lc code=start
class Solution:
    '''
    The idea is to use smaller numbers before the larger ones
    The rule is simple: if "I", attach the next smallest available number to the array
    If "D", add 1 to each preceding number until the element is smaller than stack top
    then attach the original stack top
    '''

    def smallestNumber(self, pattern: str) -> str:
        result = [1]
        for c in pattern:
            if c == "I":
                nxt = result[-1] + 1
                while nxt in result: nxt += 1
            else:
                nxt = result[-1]
                i = len(result)-1
                while i >= 0 and result[i] >= nxt:
                    result[i] += 1
                    i -= 1
            result.append(nxt)
        return "".join([str(i) for i in result])
# @lc code=end

