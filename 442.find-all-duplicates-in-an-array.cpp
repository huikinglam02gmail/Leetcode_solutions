/*
 * @lc app=leetcode id=442 lang=cpp
 *
 * [442] Find All Duplicates in an Array
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /*
    Use array index as hash_key
    when you see a number i in an array, just add the array length n to the ith element
    the original number can be recovered by getting num % n
    duplicates would be added 2 times and can be easily identified by the corresponding index
    */
    std::vector<int> findDuplicates(std::vector<int>& nums) {
        int n = nums.size();
        for (int num : nums) nums[((num % n) + n - 1) % n] += n;
        std::vector<int> result;
        for (int i = 0; i < n; i++) {
            if (nums[i] > 2 * n) result.push_back(i + 1);
        }
        return result;
    }
};

// @lc code=end

