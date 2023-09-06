/*
 * @lc app=leetcode id=725 lang=csharp
 *
 * [725] Split Linked List in Parts
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
 *     public ListNode(int val = 0, ListNode next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode[] SplitListToParts(ListNode head, int k) {
        ListNode temp = head;
        int n = 0;
        
        while (temp != null) {
            n++;
            temp = temp.next;
        }
        
        ListNode[] result = new ListNode[k];
        temp = head;
        
        for (int j = 0; j < k; j++) {
            ListNode tempHead = temp;
            int thres = (j < n % k) ? n / k + 1 : n / k;
            
            if (thres > 0) {
                int count = 0;
                ListNode tempTail = null;
                
                while (count < thres) {
                    count++;
                    
                    if (count == thres) {
                        tempTail = temp;
                    }
                    
                    temp = temp.next;
                }
                
                if (tempTail != null) {
                    tempTail.next = null;
                }
                
            }
            
            result[j] = tempHead;
        }
        
        return result;
    }
}

// @lc code=end

