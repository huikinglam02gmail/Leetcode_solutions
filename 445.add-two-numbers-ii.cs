/*
 * @lc app=leetcode id=445 lang=csharp
 *
 * [445] Add Two Numbers II
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
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        var stack1 = new Stack<ListNode>();
        var stack2 = new Stack<ListNode>();
        var head1 = new ListNode(0, l1);
        var head2 = new ListNode(0, l2);
        var temp1 = head1;
        var temp2 = head2;

        while (temp1.next != null) {
            stack1.Push(temp1);
            temp1 = temp1.next;
        }

        while (temp2.next != null) {
            stack2.Push(temp2);
            temp2 = temp2.next;
        }

        if (stack1.Count < stack2.Count) {
            var tempStack = stack1;
            stack1 = stack2;
            stack2 = tempStack;

            var tempNode = temp1;
            temp1 = temp2;
            temp2 = tempNode;

            var tempHead = head1;
            head1 = head2;
            head2 = tempHead;
        }

        while (stack1.Count > 0) {
            int a, b;
            if (stack2.Count > 0) {
                a = temp1.val + temp2.val;
                temp2 = stack2.Pop();
            } else {
                a = temp1.val;
            }

            b = a % 10;
            a /= 10;

            stack1.Peek().val += a;
            temp1.val = b;
            temp1 = stack1.Pop();
        }

        return head1.val > 0 ? head1 : head1.next;
    }
}

// @lc code=end

