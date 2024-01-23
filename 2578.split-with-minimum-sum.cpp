/*
 * @lc app=leetcode id=2578 lang=cpp
 *
 * [2578] Split With Minimum Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * Sort the digits, add up odd and even digits
     */
    int splitNum(int num) {
        std::vector<int> arr;
        while (num > 0) {
            arr.push_back(num % 10);
            num /= 10;
        }

        std::sort(arr.begin(), arr.end());

        std::vector<std::string> newArr(2, "");
        for (int i = 0; i < arr.size(); i++) {
            newArr[i % 2] += std::to_string(arr[i]);
        }

        return std::stoi(newArr[0]) + std::stoi(newArr[1]);
    }
};

// @lc code=end

