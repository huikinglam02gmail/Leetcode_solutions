/*
 * @lc app=leetcode id=1669 lang=csharp
 *
 * [1669] Merge In Between Linked Lists
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
public class Solution 
{
    public ListNode MergeInBetween(ListNode list1, int a, int b, ListNode list2) 
    {
        ListNode temp = list1;
        int step = 0;
        while (step < a - 1)
        {
            temp = temp.next;
            step++;
        }
        ListNode aNode = temp;
        while (step <= b)
        {
            temp = temp.next;
            step++;
        }
        ListNode bNode = temp;
        aNode.next = list2;
        temp = aNode;
        while (temp.next != null)
        {
            temp = temp.next;
        }
        temp.next = bNode;
        return list1;
    }
}
// @lc code=end

