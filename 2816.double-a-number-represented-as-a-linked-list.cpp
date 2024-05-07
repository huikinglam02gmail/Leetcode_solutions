/*
 * @lc app=leetcode id=2816 lang=cpp
 *
 * [2816] Double a Number Represented as a Linked List
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
#include <stack>
using namespace std;

class Solution {
public:
    /*
    Use stack to process from back to front
    */
    ListNode* doubleIt(ListNode* head) {
        if (!head) return nullptr;

        stack<ListNode*> stack;
        ListNode* temp = head;
        while (temp) {
            stack.push(temp);
            temp = temp->next;
        }
        bool addOne = false;
        while (!stack.empty()) {
            temp = stack.top();
            stack.pop();
            temp->val *= 2;
            if (addOne) {
                temp->val += 1;
                addOne = false;
            }
            if (temp->val >= 10) {
                addOne = true;
                if (stack.empty()) {
                    stack.push(new ListNode(0, temp));
                }
            }
            temp->val %= 10;
        }
        return temp;
    }
};

// @lc code=end

