/*
 * @lc app=leetcode id=1760 lang=cpp
 *
 * [1760] Minimum Limit of Balls in a Bag
 */

// @lc code=start
#include <vector>
#include <algorithm>
using std::max;
using std::max_element;
using std::vector;
class Solution {
private:
    int OperationsToMake(int maxN, const vector<int>& nums)
    {
        int result = 0;
        for (int num : nums)
        {
            result += num / maxN;
            if (num % maxN == 0)
            {
                result -= 1;
            }
        }
        return result;
    }

public:
    int minimumSize(vector<int>& nums, int maxOperations) 
    {
        int l = 1;
        int r = *max_element(nums.begin(), nums.end());

        while (l < r)
        {
            int mid = l + (r - l) / 2;
            if (OperationsToMake(mid, nums) <= maxOperations)
            {
                r = mid;
            }
            else
            {
                l = mid + 1;
            }
        }

        return l;
    }
};
// @lc code=end

