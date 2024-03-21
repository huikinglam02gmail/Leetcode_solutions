/*
 * @lc app=leetcode id=206 lang=csharp
 *
 * [206] Reverse Linked List
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

public class Solution {
    /*
    Keep three nodes, and flip the next arrow of the middle node.
    */
    public ListNode ReverseList(ListNode head) {
        ListNode temp = head;
        ListNode tempPrev = null;
        while (temp != null) {
            ListNode tempNext = temp.next;
            temp.next = tempPrev;
            tempPrev = temp;
            temp = tempNext;
        }
        head = tempPrev;
        return head;
    }
}

// @lc code=end

