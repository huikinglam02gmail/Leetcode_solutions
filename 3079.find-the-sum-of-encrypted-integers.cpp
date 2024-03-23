/*
 * @lc app=leetcode id=3079 lang=cpp
 *
 * [3079] Find the Sum of Encrypted Integers
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <string>

class Solution {
public:
    int sumOfEncryptedInt(std::vector<int>& nums) {
        int result = 0;
        for (int num : nums) {
            std::unordered_set<int> numSet;
            std::string numString = std::to_string(num);
            for (char c : numString) {
                numSet.insert(c - '0');
            }
            int maxDigit = 0;
            for (int digit : numSet) {
                maxDigit = std::max(maxDigit, digit);
            }
            std::string maxDigitStr(numString.length(), maxDigit + '0');
            result += std::stoi(maxDigitStr);
        }
        return result;
    }
};

// @lc code=end

