/*
 * @lc app=leetcode id=421 lang=cpp
 *
 * [421] Maximum XOR of Two Numbers in an Array
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int findMaximumXOR(std::vector<int>& nums) 
    {
        int result = 0;
        int numberOfLevels = 31;

        for (int i = numberOfLevels - 1; i >= 0; i--) 
        {
            std::unordered_set<int> prefixes;

            for (int num : nums) 
            {
                prefixes.insert(num >> i);
            }

            result <<= 1;

            for (int prefix : prefixes) 
            {
                if (prefixes.count((result + 1) ^ prefix)) 
                {
                    result += 1;
                    break;
                }
            }
        }

        return result;
    }
};

// @lc code=end

