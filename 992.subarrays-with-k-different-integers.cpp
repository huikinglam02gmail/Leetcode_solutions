/*
 * @lc app=leetcode id=992 lang=cpp
 *
 * [992] Subarrays with K Different Integers
 */

// @lc code=start
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    /*
    A sliding window problem
    It is rather hard to count subarrays with exactly k different integers
    But we can tweak the question a little bit:
    number of good subarrays = number of subarray with at most k different integers - number of subarrays with at most k - 1 different integers 
    */
    int subarraysWithLessThanOrEqualToKDistinct(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        int l = 0;
        int res = 0;
        for (int r = 0; r < nums.size(); r++) {
            counter[nums[r]]++;
            while (counter.size() > k) {
                counter[nums[l]]--;
                if (counter[nums[l]] == 0)
                    counter.erase(nums[l]);
                l++;
            }
            res += r - l + 1;
        }
        return res;
    }
    
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return subarraysWithLessThanOrEqualToKDistinct(nums, k) - subarraysWithLessThanOrEqualToKDistinct(nums, k - 1);
    }
};

// @lc code=end

