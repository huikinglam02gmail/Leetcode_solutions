/*
 * @lc app=leetcode id=2231 lang=cpp
 *
 * [2231] Largest Number After Digit Swaps by Parity
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <string>

using std::string;

class Solution {
public:
    int largestInteger(int num) {
        std::vector<int> parity[2];
        std::vector<int> parityDigits[2];
        std::string numString = std::to_string(num);
        for (int i = 0; i < numString.size(); i++)
        {
            int digit = numString[i] - '0';
            parity[digit % 2].push_back(i);
            parityDigits[digit % 2].push_back(digit);
        }

        for (auto& list : parityDigits) {
            std::sort(list.rbegin(), list.rend());
        }

        std::string final(std::to_string(num).length(), ' ');

        for (int j = 0; j < 2; ++j) {
            for (size_t i = 0; i < parity[j].size(); ++i) {
                final[parity[j][i]] = static_cast<char>(parityDigits[j][i] + '0');
            }
        }

        return std::stoi(final);
    }
};

// @lc code=end

