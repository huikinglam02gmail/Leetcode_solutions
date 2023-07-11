/*
 * @lc app=leetcode id=863 lang=cpp
 *
 * [863] All Nodes Distance K in Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<queue>
using std::queue;
using std::unordered_map;
using std::unordered_set;
using std::vector;
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        unordered_map<int, unordered_set<int>> graph{};
        queue<TreeNode*> q1{};
        q1.push(root);
        graph.insert({root -> val, unordered_set<int>{}});

        while (q1.size() > 0) {
            TreeNode* node = q1.front();
            q1.pop();

            if (node -> left != NULL) {
                graph.insert({node -> left -> val, unordered_set<int>{}});
                graph[node -> val].insert(node -> left -> val);
                graph[node -> left -> val].insert(node -> val);
                q1.push(node -> left);
            }

            if (node -> right != NULL) {
                graph.insert({node -> right -> val, unordered_set<int>{}});
                graph[node -> val].insert(node -> right -> val);
                graph[node -> right -> val].insert(node -> val);
                q1.push(node -> right);
            }
        }

        queue<int> q2 {};
        unordered_set<int> visited {};
        q2.push(target -> val);
        visited.insert(target -> val);
        int steps = 0;
        vector<int> result {};

        while (q2.size() > 0) {
            int count = q2.size();

            for (int i = 0; i < count; i++) {
                int node = q2.front();
                q2.pop();

                if (steps == k) {
                    result.push_back(node);
                }
                else {
                    for (int next : graph[node]) {
                        if (visited.find(next) == visited.end()) {
                            visited.insert(next);
                            q2.push(next);
                        }
                    }
                }
            }

            if (steps == k) {
                return result;
            }

            steps++;
        }

        return result;
    }
};
// @lc code=end

