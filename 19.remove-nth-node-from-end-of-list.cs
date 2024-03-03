/*
 * @lc app=leetcode id=19 lang=csharp
 *
 * [19] Remove Nth Node From End of List
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
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        if (head.next == null) return null;
        
        int counter = 0;
        ListNode temp = head;
        
        while (temp.next != null) {
            counter++;
            temp = temp.next;
        }
        
        int total = counter;
        
        if (total < n - 1) {
            return null;
        } else if (total == n - 1) {
            return head.next;
        } else {
            counter = 0;
            temp = head;
            ListNode temp1 = temp;
            
            while (counter < total - n + 1) {
                counter++;
                temp1 = temp;
                temp = temp.next;
            }
            
            temp1.next = temp.next;
            return head;
        }
    }
}

// @lc code=end

