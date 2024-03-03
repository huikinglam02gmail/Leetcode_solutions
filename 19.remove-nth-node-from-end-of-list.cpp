/*
 * @lc app=leetcode id=19 lang=cpp
 *
 * [19] Remove Nth Node From End of List
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
 *     ListNode(int val = 0, ListNode *next = nullptr) : val(val), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head->next) return nullptr;
        
        int counter = 0;
        ListNode* temp = head;
        
        while (temp->next) {
            counter++;
            temp = temp->next;
        }
        
        int total = counter;
        
        if (total < n - 1) {
            return nullptr;
        } else if (total == n - 1) {
            return head->next;
        } else {
            counter = 0;
            temp = head;
            ListNode* temp1 = nullptr;
            
            while (counter < total - n + 1) {
                counter++;
                temp1 = temp;
                temp = temp->next;
            }
            
            temp1->next = temp->next;
            return head;
        }
    }
};

// @lc code=end

