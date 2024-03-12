#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    '''
    Make a new dummy node with value 0 and prefix sum 0. Set its next to head
    Traverse the linked list
    Record the prefix sum S during the traversal in a hash table
    hash_table[S] = [node1, node2, ... , nodek]
    Then go back to the dummy node, set node.next = hash_table[S][-1].next
    The next node's prefix sum would be S + next_node.val   
    '''

    
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        S, temp, hash_table = 0, dummy, {}
        while temp:
            S += temp.val
            if S not in hash_table: hash_table[S] = []
            hash_table[S].append(temp)
            temp = temp.next
        
        temp, prefix = dummy, 0
        while temp:
            prefix += temp.val
            temp.next = hash_table[prefix][-1].next
            temp = temp.next
        return dummy.next
# @lc code=end

