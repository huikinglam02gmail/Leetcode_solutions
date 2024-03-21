/*
 * @lc app=leetcode id=206 lang=cpp
 *
 * [206] Reverse Linked List
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
    /*
    Keep three nodes, and flip the next arrow of the middle node.
    */
    ListNode* reverseList(ListNode* head) {
        ListNode* temp = head;
        ListNode* tempPrev = nullptr;
        while (temp != nullptr) {
            ListNode* tempNext = temp->next;
            temp->next = tempPrev;
            tempPrev = temp;
            temp = tempNext;
        }
        head = tempPrev;
        return head;
    }
};
// @lc code=end

