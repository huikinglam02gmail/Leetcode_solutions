/*
 * @lc app=leetcode id=456 lang=cpp
 *
 * [456] 132 Pattern
 */

// @lc code=start
#include <vector>
#include <stack>
#include <utility> // For std::pair

class Solution {
public:
    bool find132pattern(std::vector<int>& nums) {
        std::stack<std::pair<int, int>> stack;
        
        for (int num : nums) {
            int thisMin = num;
            
            if (!stack.empty()) {
                thisMin = std::min(thisMin, stack.top().second);
            }
            
            while (!stack.empty() && num >= stack.top().first) {
                stack.pop();
            }
            
            if (!stack.empty() && stack.top().second < num) {
                return true;
            }
            
            stack.push(std::make_pair(num, thisMin));
        }
        
        return false;
    }
};

// @lc code=end

