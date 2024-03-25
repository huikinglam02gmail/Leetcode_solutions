/*
 * @lc app=leetcode id=2074 lang=csharp
 *
 * [2074] Reverse Nodes in Even Length Groups
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
    /*
    Keep track of current level length.
    If current level length is even, we record the end of last level. Then move to the next node and start reversing the linked list up to current level length or end
    Then point last.next to the end
    Move the pointer forward by current level length's step
    */
    public ListNode ReverseEvenLengthGroups(ListNode head)
    {
        int currentLevelLength = 1;
        ListNode temp = new ListNode(-1);
        temp.next = head;
        while (temp != null)
        {
            int steps = 0;
            ListNode temp1 = temp;
            while (steps <= currentLevelLength && temp1 != null)
            {
                temp1 = temp1.next;
                steps += 1;
            }
            if (steps % 2 != 0) ReverseLLBetweenTwoNodes(temp, temp1);
            steps = 0;
            while (steps < currentLevelLength && temp != null)
            {
                temp = temp.next;
                steps += 1;
            }
            currentLevelLength += 1;
        }
        return head;
    }

    private void ReverseLLBetweenTwoNodes(ListNode nodePrev, ListNode nodeAfter)
    {
        ListNode temp1 = nodePrev.next;
        ListNode temp1Prev = nodeAfter;
        while (temp1 != nodeAfter)
        {
            ListNode temp1Next = temp1.next;
            temp1.next = temp1Prev;
            temp1Prev = temp1;
            temp1 = temp1Next;
        }
        nodePrev.next = temp1Prev;
    }
}
  

// @lc code=end

