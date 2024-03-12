/*
 * @lc app=leetcode id=1171 lang=csharp
 *
 * [1171] Remove Zero Sum Consecutive Nodes from Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
using System.Collections.Generic;

public class Solution {
    public ListNode RemoveZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int S = 0;
        ListNode temp = dummy;
        Dictionary<int, ListNode> hashTable = new Dictionary<int, ListNode>();

        while (temp != null) {
            S += temp.val;
            if (!hashTable.ContainsKey(S)) {
                hashTable[S] = temp;
            } else {
                hashTable[S].next = temp.next;
            }
            temp = temp.next;
        }

        temp = dummy;
        S = 0;
        while (temp != null) {
            S += temp.val;
            temp.next = hashTable[S].next;
            temp = temp.next;
        }

        return dummy.next;
    }
}

// @lc code=end

