#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        index, result = 1, [1]
        while index < n:
            current, counter, next_result = 0, 0, []
            for i in range(len(result)):
                if result[i] != current:
                    if current != 0:
                        next_result.append(counter)
                        next_result.append(current)
                    current, counter = result[i], 1
                else:
                    counter += 1
            next_result.append(counter)
            next_result.append(current)
            index += 1
            result = next_result
        string = ''
        for i in result:
            string = string + str(i)
        return string
# @lc code=end

