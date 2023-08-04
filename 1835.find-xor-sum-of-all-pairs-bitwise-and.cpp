/*
 * @lc app=leetcode id=1835 lang=cpp
 *
 * [1835] Find XOR Sum of All Pairs Bitwise AND
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int getXORSum(std::vector<int>& arr1, std::vector<int>& arr2) {
        int numberOfDigits1 = GetNumberOfDigits(arr1);
        int numberOfDigits2 = GetNumberOfDigits(arr2);
        int numberOfDigits = std::max(numberOfDigits1, numberOfDigits2);

        if (numberOfDigits1 > numberOfDigits2) {
            std::swap(arr1, arr2);
        }

        std::vector<int> cnts2(numberOfDigits, 0);
        for (int num : arr2) {
            for (int j = 0; j < numberOfDigits; j++) {
                if ((num & (1 << j)) > 0) {
                    cnts2[j]++;
                }
            }
        }

        int result = 0;
        for (int num : arr1) {
            for (int j = 0; j < numberOfDigits; j++) {
                if ((num & (1 << j)) > 0) {
                    result ^= (1 << j) * (cnts2[j] % 2);
                }
            }
        }

        return result;
    }

private:
    int GetNumberOfDigits(const std::vector<int>& arr) {
        int maxVal = 0;
        for (int num : arr) {
            maxVal = std::max(maxVal, num);
        }
        return static_cast<int>(std::bitset<32>(maxVal).size());
    }
};

// @lc code=end

