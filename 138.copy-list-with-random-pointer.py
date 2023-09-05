#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional


class Solution:
    '''
    -10^4 <= Node.val <= 10^4
    0 <= Node.val + 10000 <= 20000 
    Modify the Node at index values to i * 20001 + (node[i].val + 10000)
    For each Node, Record hashTable[node val] = index; hashTableRandom[node val] = nextRandomNode's node val
    Finally recover the list
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        i = 0
        newList = []
        indexMap = {}
        while temp:
            newNode = Node(temp.val)
            if newList:
                newList[-1].next = newNode
            newList.append(newNode)
            temp.val = i * 20001 + (temp.val + 10000)
            indexMap[temp.val] = i
            temp = temp.next
            i += 1
        temp = head
        while temp:
            if temp.random != None:
                newList[indexMap[temp.val]].random = newList[indexMap[temp.random.val]]
            temp = temp.next
        return None if len(newList) == 0 else newList[0]
# @lc code=end

