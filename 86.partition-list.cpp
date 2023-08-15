/*
 * @lc app=leetcode id=86 lang=cpp
 *
 * [86] Partition List
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
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* temp = head;
        ListNode* dummy1 = new ListNode(-101);
        ListNode* dummy2 = new ListNode(101);
        ListNode* temp1 = dummy1;
        ListNode* temp2 = dummy2;
        
        while (temp != nullptr) {
            if (temp->val < x) {
                temp1->next = temp;
                temp1 = temp1->next;
            } else {
                temp2->next = temp;
                temp2 = temp2->next;
            }
            temp = temp->next;
        }
        
        temp2->next = nullptr;
        temp1->next = dummy2->next;
        
        ListNode* result = dummy1->next;
        delete dummy1;
        delete dummy2;
        
        return result;
    }
};
// @lc code=end

