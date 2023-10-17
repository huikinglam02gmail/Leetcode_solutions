/*
 * @lc app=leetcode id=1361 lang=cpp
 *
 * [1361] Validate Binary Tree Nodes
 */

// @lc code=start
/**
 * @lc app=leetcode id=1361 lang=cpp
 *
 * [1361] Validate Binary Tree Nodes
 */

#include <vector>
using namespace std;

class Solution {
private:
    vector<int> parent;

public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        parent = vector<int>(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int run = 0; run < 2; run++) {
            vector<int>& data = (run == 0) ? leftChild : rightChild;
            for (int i = 0; i < n; i++) {
                int child = data[i];
                if (child >= 0) {
                    int parent_i = Find(i);
                    int parent_child = Find(child);
                    if (parent_i == parent_child) {
                        return false;
                    }
                    parent[child] = parent_i;
                }
            }
        }

        int rootCount = 0;
        for (int i = 0; i < n; i++) {
            if (parent[i] == i) {
                rootCount++;
            }
        }

        return rootCount == 1;
    }

private:
    int Find(int x) {
        while (parent[x] != x) {
            x = parent[x];
        }
        return x;
    }
};

// @lc code=end

