/*
 * @lc app=leetcode id=2487 lang=cpp
 *
 * [2487] Remove Nodes From Linked List
 */

// @lc code=start
#include <stack>

class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        ListNode* prevHead = new ListNode(100001, head);
        ListNode* temp = head;
        std::stack<ListNode*> stack;
        stack.push(prevHead);
        while (temp) {
            while (!stack.empty() && stack.top()->val < temp->val) {
                stack.pop();
            }
            stack.top()->next = temp;
            stack.push(temp);
            temp = temp->next;
        }
        return prevHead->next;
    }
};

// @lc code=end

