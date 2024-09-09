#
# @lc app=leetcode id=2326 lang=python3
#
# [2326] Spiral Matrix IV
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    '''
    Keep the row and column limits and traverse
    '''
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for j in range(n)] for i in range(m)]
        limits = [0, m - 1, 0, n - 1]
        pos = [0, 0]
        temp = head
        direction = 0
        while temp:
            matrix[pos[0]][pos[1]] = temp.val
            temp = temp.next
            if direction == 0:
                if pos[1] < limits[3]:
                    pos[1] += 1
                else:
                    pos[0] += 1
                    limits[0] += 1
                    direction = 1
            elif direction == 1:
                if pos[0] < limits[1]:
                    pos[0] += 1
                else:
                    pos[1] -= 1
                    limits[3] -= 1
                    direction = 2
            elif direction == 2:
                if pos[1] > limits[2]:
                    pos[1] -= 1
                else:
                    pos[0] -= 1
                    limits[1] -= 1
                    direction = 3
            else:
                if pos[0] > limits[0]:
                    pos[0] -= 1
                else:
                    pos[1] += 1
                    limits[2] += 1
                    direction = 0
        return matrix
# @lc code=end

