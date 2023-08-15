/*
 * @lc app=leetcode id=86 lang=csharp
 *
 * [86] Partition List
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
public ListNode Partition(ListNode head, int x) {
        ListNode temp = head;
        ListNode dummy1 = new ListNode(-101);
        ListNode dummy2 = new ListNode(101);
        ListNode temp1 = dummy1;
        ListNode temp2 = dummy2;
        
        while (temp != null) {
            if (temp.val < x) {
                temp1.next = temp;
                temp1 = temp1.next;
            } else {
                temp2.next = temp;
                temp2 = temp2.next;
            }
            temp = temp.next;
        }
        
        temp2.next = null;
        temp1.next = dummy2.next;
        
        return dummy1.next;
    }
}
// @lc code=end

