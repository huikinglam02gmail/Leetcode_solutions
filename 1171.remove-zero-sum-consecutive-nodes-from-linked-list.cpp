/*
 * @lc app=leetcode id=1171 lang=cpp
 *
 * [1171] Remove Zero Sum Consecutive Nodes from Linked List
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
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <unordered_map>

class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        int S = 0;
        ListNode* temp = dummy;
        std::unordered_map<int, ListNode*> hashTable;

        while (temp) {
            S += temp->val;
            if (!hashTable.count(S)) {
                hashTable[S] = temp;
            } else {
                hashTable[S]->next = temp->next;
            }
            temp = temp->next;
        }

        temp = dummy;
        S = 0;
        while (temp) {
            S += temp->val;
            temp->next = hashTable[S]->next;
            temp = temp->next;
        }

        return dummy->next;
    }
};

// @lc code=end

