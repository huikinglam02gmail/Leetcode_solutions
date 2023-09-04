/*
 * @lc app=leetcode id=141 lang=csharp
 *
 * [141] Linked List Cycle
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution
{
    /// <summary>
    /// Turtoise and hare algorithm.
    /// </summary>
    public bool HasCycle(ListNode head)
    {
        ListNode fast = head;
        ListNode slow = head;

        if (head == null)
        {
            return false;
        }

        while (fast.next != null && slow.next != null && fast.next.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow)
            {
                return true;
            }
        }

        return false;
    }
}
// @lc code=end

