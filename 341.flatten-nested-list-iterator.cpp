/*
 * @lc app=leetcode id=341 lang=cpp
 *
 * [341] Flatten Nested List Iterator
 */

// @lc code=start
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

#include <vector>
#include <stack>
#include <utility>

using std::make_pair;

class NestedIterator {
private:
    std::stack<std::pair<std::vector<NestedInteger>*, int>> stack;

public:
    NestedIterator(std::vector<NestedInteger> &nestedList) {
        stack.push(make_pair(&nestedList, 0));
    }

    int next() {
        if (hasNext()) {
            auto [nestedList, index] = stack.top();
            stack.top().second++;
            return (*nestedList)[index].getInteger();
        }
        return -1; // Return -1 if there's no next element.
    }

    bool hasNext() {
        while (!stack.empty()) {
            auto [nestedList, index] = stack.top();
            if (index == nestedList->size()) {
                stack.pop();
            } else {
                if ((*nestedList)[index].isInteger()) {
                    return true;
                }
                stack.top().second++;
                stack.push(make_pair(&(*nestedList)[index].getList(), 0));
            }
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
// @lc code=end

