/*
 * @lc app=leetcode id=725 lang=cpp
 *
 * [725] Split Linked List in Parts
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
    std::vector<ListNode*> splitListToParts(ListNode* head, int k) {
        ListNode* temp = head;
        int n = 0;
        
        while (temp != nullptr) {
            n++;
            temp = temp->next;
        }
        
        std::vector<ListNode*> result(k);
        temp = head;
        
        for (int j = 0; j < k; j++) {
            ListNode* tempHead = temp;
            int thres = (j < n % k) ? n / k + 1 : n / k;
            
            if (thres > 0) {
                int count = 0;
                ListNode* tempTail = nullptr;
                
                while (count < thres) {
                    count++;
                    
                    if (count == thres) {
                        tempTail = temp;
                    }
                    
                    temp = temp->next;
                }
                
                if (tempTail != nullptr) {
                    tempTail->next = nullptr;
                }
                
            }
            
            result[j] = tempHead;
        }
        
        return result;
    }
};
// @lc code=end

