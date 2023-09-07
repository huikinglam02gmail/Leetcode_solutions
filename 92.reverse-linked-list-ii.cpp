/*
 * @lc app=leetcode id=92 lang=cpp
 *
 * [92] Reverse Linked List II
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
#include<stack>
using std::stack;

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int i = 1;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* temp = head;
        ListNode* start = dummy;
        std::stack<ListNode*> stack {};

        while (temp != nullptr) {
            if (left <= i && i <= right) {
                stack.push(temp);
            }
            if (i == left) {
                start = prev;
            }
            prev = prev->next;
            temp = temp->next;
            i++;
        }

        ListNode* last = (stack.size() > 0) ? stack.top()->next : nullptr;

        while (stack.size() > 0) {
            start->next = stack.top();
            stack.pop();
            start = start->next;
        }

        start->next = last;

        return dummy->next;
    }
};

// @lc code=end

