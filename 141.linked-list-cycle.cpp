/*
 * @lc app=leetcode id=141 lang=cpp
 *
 * [141] Linked List Cycle
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * Turtoise and hare algorithm.
     */
    bool hasCycle(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;

        if (head == nullptr) {
            return false;
        }

        while (fast->next != nullptr && slow->next != nullptr && fast->next->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;

            if (fast == slow) {
                return true;
            }
        }

        return false;
    }
};
// @lc code=end

