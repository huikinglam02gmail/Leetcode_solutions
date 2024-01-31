/*
 * @lc app=leetcode id=739 lang=cpp
 *
 * [739] Daily Temperatures
 */

// @lc code=start
#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        int n = temperatures.size();
        std::vector<int> result(n, 0);
        std::stack<int> stack;

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && temperatures[stack.top()] <= temperatures[i]) {
                stack.pop();
            }

            if (!stack.empty()) {
                result[i] = stack.top() - i;
            }

            stack.push(i);
        }

        return result;
    }
};

// @lc code=end

