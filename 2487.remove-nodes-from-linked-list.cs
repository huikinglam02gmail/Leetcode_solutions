/*
 * @lc app=leetcode id=2487 lang=csharp
 *
 * [2487] Remove Nodes From Linked List
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public ListNode RemoveNodes(ListNode head) {
        ListNode prevHead = new ListNode(100001, head);
        ListNode temp = head;
        Stack<ListNode> stack = new Stack<ListNode>();
        stack.Push(prevHead);
        while (temp != null) {
            while (stack.Count > 0 && stack.Peek().val < temp.val) {
                stack.Pop();
            }
            stack.Peek().next = temp;
            stack.Push(temp);
            temp = temp.next;
        }
        return prevHead.next;
    }
}

// @lc code=end

