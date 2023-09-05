/*
 * @lc app=leetcode id=138 lang=cpp
 *
 * [138] Copy List with Random Pointer
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;

        Node* temp = head;
        int i = 0;
        std::vector<Node*> newList;
        std::unordered_map<int, int> indexMap;

        while (temp != nullptr) {
            Node* newNode = new Node(temp->val);
            if (!newList.empty()) {
                newList.back()->next = newNode;
            }
            newList.push_back(newNode);

            temp->val = i * 20001 + (temp->val + 10000);
            indexMap[temp->val] = i;
            temp = temp->next;
            i++;
        }

        temp = head;

        while (temp != nullptr) {
            if (temp->random != nullptr) {
                newList[indexMap[temp->val]]->random = newList[indexMap[temp->random->val]];
            }
            temp = temp->next;
        }

        return newList.empty() ? nullptr : newList[0];
    }
};
// @lc code=end

