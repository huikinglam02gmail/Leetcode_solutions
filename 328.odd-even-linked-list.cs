/*
 * @lc app=leetcode id=328 lang=csharp
 *
 * [328] Odd Even Linked List
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
    public ListNode OddEvenList(ListNode head) 
    {
        if (head == null || head.next == null)
        {
            return head;
        }
        else
        {
            ListNode odd = null;
            ListNode even = null;
            ListNode tempOdd = null;
            ListNode tempEven = null;
            int count = 0;
            ListNode temp = head;
            while (temp != null)
            {
                if (count % 2 == 0)
                {
                    if (count == 0)
                    {
                        odd = temp;
                        tempOdd = temp;
                    }
                    else
                    {
                        tempOdd.next = temp;
                        tempOdd = tempOdd.next;
                    }
                }
                else
                {
                    if (count == 1)
                    {
                        even = temp;
                        tempEven = temp;
                    }
                    else
                    {
                        tempEven.next = temp;
                        tempEven = tempEven.next;
                    }
                }
                temp = temp.next;
                count++;
            }
            tempEven.next = null;
            tempOdd.next = even;
            return odd;
        }
    }
}
// @lc code=end

