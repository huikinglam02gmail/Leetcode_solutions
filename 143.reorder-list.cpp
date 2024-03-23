/*
 * @lc app=leetcode id=143 lang=cpp
 *
 * [143] Reorder List
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
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(nullptr) {}
 * };
 */

class Solution {
public:
    /**
     * Use turtle and hare algorithm to find mid point.
     * Reverse the latter half
     * Merge the two LL
     */
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* sPrev = nullptr;
        while (fast && fast->next) {
            sPrev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        if (fast) {
            sPrev = sPrev->next;
            slow = slow->next;
        }
        sPrev->next = nullptr;
        sPrev = sPrev->next;
        while (slow) {
            ListNode* sNext = slow->next;
            slow->next = sPrev;
            sPrev = slow;
            slow = sNext;
        }
        ListNode* temp1 = head;
        ListNode* temp2 = sPrev;
        while (temp1) {
            ListNode* temp1Next = temp1->next;
            temp1->next = temp2;
            temp2 = temp1Next;
            temp1 = temp1->next;
        }
    }
};

// @lc code=end

