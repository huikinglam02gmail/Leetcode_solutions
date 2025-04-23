#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = {}
        for i in range(1,n + 1):
            key, str_i = 0, str(i)
            for j in range(len(str_i)): key += int(str_i[j])
            group[key] = group.get(key, 0) + 1
        
        values = sorted(group.values(), reverse = True)
        result = 0
        for value in values:
            if value == values[0]: result += 1
        return result
            
# @lc code=end

