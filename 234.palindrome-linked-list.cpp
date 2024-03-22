/*
 * @lc app=leetcode id=234 lang=cpp
 *
 * [234] Palindrome Linked List
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
using namespace std;

class Solution {
public:
    /*
    Turtle and hare + reverse linked list:
    If we follow the turtle and hare algorithm, we know that:
    1. If the number of nodes in the LL is odd, fast will stay on the last node.
    2. If the number of nodes in the LL is even, fast will be null
    For both cases, slow will be at n // 2 th node
    If we reverse the LL while slow progresses, keeping track of sNext and sPrev:
    1. If the number of nodes in the LL is odd s = sNext
    Then we compare values of s and sPrev and progress them.
    */
    bool isPalindrome(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* sNext = slow->next;
        ListNode* sPrev = nullptr;
        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            slow->next = sPrev;
            sPrev = slow;
            slow = sNext;
            sNext = slow->next;
        }
        if (fast != nullptr) {
            slow = slow->next;
        }
        while (slow != nullptr) {
            if (slow->val != sPrev->val) return false;
            slow = slow->next;
            sPrev = sPrev->next;
        }
        return true;
    }
};

// @lc code=end

