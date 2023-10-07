/*
 * @lc app=leetcode id=1932 lang=cpp
 *
 * [1932] Merge BSTs to Create Single BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <vector>
#include <unordered_map>
#include <queue>
#include <unordered_set>

struct BSTQueueNode {
    TreeNode* current;
    TreeNode* leftParent;
    TreeNode* rightParent;
    int minimum;
    int maximum;
    BSTQueueNode(TreeNode* current, TreeNode* leftParent, TreeNode* rightParent, int minimum, int maximum)
        : current(current), leftParent(leftParent), rightParent(rightParent), minimum(minimum), maximum(maximum) {}
};

class Solution {
public:
    TreeNode* canMerge(std::vector<TreeNode*>& trees) {
        if (trees.size() == 1) {
            return trees[0];
        }

        std::unordered_map<int, int> hashTable;

        for (int i = 0; i < trees.size(); i++) {
            hashTable[trees[i]->val] = i;
            rootValSet.insert(trees[i]->val);
        }

        for (auto tree : trees) {
            leafValInHashTable(tree);
        }

        if (rootValSet.size() == 1) {
            int rootVal = 0;
            for (int nodeVal : rootValSet) {
                rootVal = nodeVal;
            }
            TreeNode* root = trees[hashTable[rootVal]];
            std::queue<BSTQueueNode> dq;
            dq.push(BSTQueueNode(root, nullptr, nullptr, 0, 50001));

            while (!dq.empty()) {
                BSTQueueNode nodeInfo = dq.front();
                dq.pop();
                TreeNode* node = nodeInfo.current;
                TreeNode* leftParent = nodeInfo.leftParent;
                TreeNode* rightParent = nodeInfo.rightParent;
                int minimum = nodeInfo.minimum;
                int maximum = nodeInfo.maximum;

                if (node->left) {
                    dq.push(BSTQueueNode(node->left, nullptr, node, minimum, node->val));
                }
                if (node->right) {
                    dq.push(BSTQueueNode(node->right, node, nullptr, node->val, maximum));
                }

                if (!node->left && !node->right && hashTable.find(node->val) != hashTable.end()) {
                    TreeNode* candidate = trees[hashTable[node->val]];
                    if (candidate->right && candidate->right->val >= maximum) {
                        continue;
                    }
                    if (candidate->left && candidate->left->val <= minimum) {
                        continue;
                    }

                    if (leftParent) {
                        leftParent->right = candidate;
                        dq.push(BSTQueueNode(candidate, leftParent, nullptr, leftParent->val, maximum));
                    }
                    if (rightParent) {
                        rightParent->left = candidate;
                        dq.push(BSTQueueNode(candidate, nullptr, rightParent, minimum, rightParent->val));
                    }
                    hashTable.erase(node->val);
                }
            }

            if (hashTable.size() == 1) {
                for (auto kvp : hashTable) {
                    return trees[kvp.second];
                }
            }
        }

        return nullptr;
    }

private:
    void leafValInHashTable(TreeNode* node) {
        if (node->left) {
            leafValInHashTable(node->left);
        }
        if (node->right) {
            leafValInHashTable(node->right);
        }
        if (!node->left && !node->right && rootValSet.count(node->val)) {
            rootValSet.erase(node->val);
        }
    }

    std::unordered_set<int> rootValSet;
};

// @lc code=end

