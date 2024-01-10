/*
 * @lc app=leetcode id=2385 lang=cpp
 *
 * [2385] Amount of Time for Binary Tree to Be Infected
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
#include <unordered_map>
#include <unordered_set>
#include <queue>

class Solution {
public:
    int amountOfTime(TreeNode* root, int start) {
        std::unordered_map<int, std::unordered_set<int>> graph;
        std::queue<TreeNode*> dq;
        dq.push(root);

        if (graph.find(root->val) == graph.end()) {
            graph[root->val] = std::unordered_set<int>();
        }

        while (!dq.empty()) {
            TreeNode* node = dq.front();
            dq.pop();

            if (node->left != nullptr) {
                graph[node->val].insert(node->left->val);
                if (graph.find(node->left->val) == graph.end()) {
                    graph[node->left->val] = std::unordered_set<int>();
                }
                graph[node->left->val].insert(node->val);
                dq.push(node->left);
            }

            if (node->right != nullptr) {
                graph[node->val].insert(node->right->val);
                if (graph.find(node->right->val) == graph.end()) {
                    graph[node->right->val] = std::unordered_set<int>();
                }
                graph[node->right->val].insert(node->val);
                dq.push(node->right);
            }
        }

        int result = -1;
        std::unordered_set<int> visited;
        std::queue<int> dq1;
        dq1.push(start);
        visited.insert(start);

        while (!dq1.empty()) {
            int count = dq1.size();
            for (int i = 0; i < count; i++) {
                int node = dq1.front();
                dq1.pop();
                for (int next : graph[node]) {
                    if (visited.find(next) == visited.end()) {
                        visited.insert(next);
                        dq1.push(next);
                    }
                }
            }
            result++;
        }

        return result;
    }
};
// @lc code=end

