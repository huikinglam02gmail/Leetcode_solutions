#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        dq = deque()
        for student in students: 
            counts[student] += 1
            dq.append(student)
        for sandwich in sandwiches:
            if counts[sandwich] == 0: return len(dq)
            else:
                while dq[0] != sandwich:
                    dq.append(dq.popleft())
                counts[dq.popleft()] -= 1
        return 0
# @lc code=end

