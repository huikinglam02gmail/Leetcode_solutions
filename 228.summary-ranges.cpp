/*
 * @lc app=leetcode id=228 lang=cpp
 *
 * [228] Summary Ranges
 */

// @lc code=start
#include <vector>
#include <string>
using std::string;
using std::to_string;
using std::vector;
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) 
    {
        vector<string> result{};
        for (int i = 0; i < nums.size(); i++)
        {
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1] + 1))
            {
                result.push_back(to_string(nums[i]));
            }
            else if (i > 0 && nums[i] == nums[i - 1] + 1)
            {
                int ind = result.back().find("->");
                result.back() = (ind < result.back().size() ? result.back().substr(0, ind) : result.back()) + "->" + to_string(nums[i]);
            }
        }
        return result;
    }
};
// @lc code=end

