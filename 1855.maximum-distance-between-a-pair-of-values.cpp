/*
 * @lc app=leetcode id=1855 lang=cpp
 *
 * [1855] Maximum Distance Between a Pair of Values
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxDistance(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::reverse(nums1.begin(), nums1.end());
        std::reverse(nums2.begin(), nums2.end());
        int result = 0;
        int n1 = nums1.size();
        int n2 = nums2.size();
        
        for (int i1 = n1 - 1; i1 >= 0; i1--) {
            int ind = std::lower_bound(nums2.begin(), nums2.end(), nums1[i1]) - nums2.begin();
            if (ind < n2 - n1 + i1 + 1) {
                result = std::max(result, n2 - n1 + i1 - ind);
            }
        }
        
        return result;
    }
};
// @lc code=end

