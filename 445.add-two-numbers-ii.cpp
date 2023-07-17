/*
 * @lc app=leetcode id=445 lang=cpp
 *
 * [445] Add Two Numbers II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode* next;
 *     ListNode(int val = 0, ListNode* next = nullptr) : val(val), next(next) {}
 * };
 */

#include <stack>
#include <utility>
using std::stack;
using std::swap;
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<ListNode*> stack1;
        stack<ListNode*> stack2;
        ListNode* head1 = new ListNode(0, l1);
        ListNode* head2 = new ListNode(0, l2);
        ListNode* temp1 = head1;
        ListNode* temp2 = head2;

        while (temp1->next != nullptr) {
            stack1.push(temp1);
            temp1 = temp1->next;
        }

        while (temp2->next != nullptr) {
            stack2.push(temp2);
            temp2 = temp2->next;
        }

        if (stack1.size() < stack2.size()) {
            swap(stack1, stack2);
            swap(temp1, temp2);
            swap(head1, head2);
        }

        while (!stack1.empty()) {
            int a, b;
            if (!stack2.empty()) {
                a = temp1->val + temp2->val;
                temp2 = stack2.top();
                stack2.pop();
            } else {
                a = temp1->val;
            }

            b = a % 10;
            a /= 10;

            stack1.top()->val += a;
            temp1->val = b;
            temp1 = stack1.top();
            stack1.pop();
        }

        return head1->val > 0 ? head1 : head1->next;
    }
};

// @lc code=end

