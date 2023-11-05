/*
 * @lc app=leetcode id=1535 lang=cpp
 *
 * [1535] Find the Winner of an Array Game
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int getWinner(std::vector<int>& arr, int k) {
        std::vector<int> stack;
        int arrMax = 0;
        
        while (!arr.empty()) {
            stack.push_back(arr.back());
            arr.pop_back();
            arrMax = std::max(arrMax, stack.back());
        }
        
        if (k >= stack.size()) {
            return arrMax;
        }
        
        int win = 0;
        while (win < k && stack.back() < arrMax) {
            int last = stack.back();
            stack.pop_back();
            int secondLast = stack.back();
            stack.pop_back();
            
            if (last <= secondLast) {
                win = 0;
            }
            
            win++;
            stack.push_back(std::max(last, secondLast));
        }
        
        return stack.back();
    }
};

// @lc code=end

