/*
 * @lc app=leetcode id=234 lang=csharp
 *
 * [234] Palindrome Linked List
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
    Turtle and hare + reverse linked list:
    If we follow the turtle and hare algorithm, we know that:
    1. If the number of nodes in the LL is odd, fast will stay on the last node.
    2. If the number of nodes in the LL is even, fast will be null
    For both cases, slow will be at n // 2 th node
    If we reverse the LL while slow progresses, keeping track of sNext and sPrev:
    1. If the number of nodes in the LL is odd s = sNext
    Then we compare values of s and sPrev and progress them.
    */
    public bool IsPalindrome(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        ListNode sNext = slow.next;
        ListNode sPrev = null;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow.next = sPrev;
            sPrev = slow;
            slow = sNext;
            sNext = slow.next;
        }
        if (fast != null) {
            slow = slow.next;
        }
        while (slow != null) {
            if (slow.val != sPrev.val) return false;
            slow = slow.next;
            sPrev = sPrev.next;
        }
        return true;
    }
}

// @lc code=end

