/*
 * @lc app=leetcode id=1993 lang=cpp
 *
 * [1993] Operations on Tree
 */

// @lc code=start
#include <vector>
#include <tuple>
#include <unordered_set>

class LockingTree {
public:
    std::vector<int> parent;
    std::vector<std::vector<int>> children;
    std::vector<std::pair<bool, int>> status;

    LockingTree(std::vector<int>& parent) {
        int n = parent.size();
        this->parent = parent;
        this->status.resize(n, {false, -1});
        this->children.resize(n);

        for (int i = 0; i < n; i++) {
            if (parent[i] >= 0) {
                this->children[parent[i]].push_back(i);
            }
        }
    }

    bool lock(int num, int user) {
        if (status[num].first) {
            return false;
        }

        status[num] = {true, user};
        return true;
    }

    bool unlock(int num, int user) {
        if (status[num].first && status[num].second == user) {
            status[num] = {false, -1};
            return true;
        }

        return false;
    }

    bool hasLockedAncestors(int node) {
        if (node == -1) {
            return false;
        } else if (status[node].first) {
            return true;
        } else {
            return hasLockedAncestors(parent[node]);
        }
    }

    bool hasLockedDescendants(int node) {
        if (status[node].first) {
            return true;
        }

        for (int child : children[node]) {
            if (hasLockedDescendants(child)) {
                return true;
            }
        }

        return false;
    }

    void unlockDescendants(int node) {
        status[node] = {false, -1};

        for (int child : children[node]) {
            unlockDescendants(child);
        }
    }

    bool upgrade(int num, int user) {
        if (hasLockedAncestors(num) || !hasLockedDescendants(num)) {
            return false;
        }

        unlockDescendants(num);
        lock(num, user);
        return true;
    }
};


/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree* obj = new LockingTree(parent);
 * bool param_1 = obj->lock(num,user);
 * bool param_2 = obj->unlock(num,user);
 * bool param_3 = obj->upgrade(num,user);
 */
// @lc code=end

