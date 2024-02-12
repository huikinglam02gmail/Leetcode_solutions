/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = -1;
        int votes = 0;
        
        for (int num : nums) {
            if (votes == 0) {
                candidate = num;
                votes = 1;
            } else {
                if (num == candidate) {
                    votes++;
                } else {
                    votes--;
                }
            }
        }
        
        return candidate;
    }
};

// @lc code=end

