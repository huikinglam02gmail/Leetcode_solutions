/*
 * @lc app=leetcode id=1669 lang=cpp
 *
 * [1669] Merge In Between Linked Lists
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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* temp = list1;
        int step = 0;
        while (step < a - 1) {
            temp = temp->next;
            step++;
        }
        ListNode* aNode = temp;
        while (step <= b) {
            temp = temp->next;
            step++;
        }
        ListNode* bNode = temp;
        aNode->next = list2;
        temp = aNode;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = bNode;
        return list1;
    }
};

// @lc code=end

