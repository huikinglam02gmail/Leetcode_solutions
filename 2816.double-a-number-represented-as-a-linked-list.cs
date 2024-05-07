/*
 * @lc app=leetcode id=2816 lang=csharp
 *
 * [2816] Double a Number Represented as a Linked List
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
using System;

public class Solution {
    /*
    Use stack to process from back to front
    */
    public ListNode DoubleIt(ListNode head) {
        if (head == null) return null;

        System.Collections.Generic.Stack<ListNode> stack = new System.Collections.Generic.Stack<ListNode>();
        ListNode temp = head;
        while (temp != null) {
            stack.Push(temp);
            temp = temp.next;
        }
        bool addOne = false;
        while (stack.Count > 0) {
            temp = stack.Pop();
            temp.val *= 2;
            if (addOne) {
                temp.val += 1;
                addOne = false;
            }
            if (temp.val >= 10) {
                addOne = true;
                if (stack.Count == 0) {
                    stack.Push(new ListNode(0, temp));
                }
            }
            temp.val %= 10;
        }
        return temp;
    }
}

// @lc code=end

