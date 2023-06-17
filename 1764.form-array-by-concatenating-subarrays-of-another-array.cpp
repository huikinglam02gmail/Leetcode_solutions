/*
 * @lc app=leetcode id=1764 lang=cpp
 *
 * [1764] Form Array by Concatenating Subarrays of Another Array
 */

// @lc code=start
#include<vector>
#include<string>
using std::string;
using std::to_string;
using std::vector;
class Solution {
private:
    string encodeNumToString(const vector<int>& nums)
    {
        string result = ""; 
        for (auto c : nums)
        {
            result += "_";
            result += to_string(c);
        }
        return result;
    }

public:
    bool canChoose(vector<vector<int>>& groups, vector<int>& nums) {
        vector<string> groupString{};
        for (vector<int> group : groups)
        {
            groupString.push_back(encodeNumToString(group));
        }
        string numsString = encodeNumToString(nums);

        int i = 0;
        int j = 0;
        while (i < numsString.size() && j < groupString.size()) {
            int ind = numsString.find(groupString[j], i);
            if (ind == -1) {
                return false;
            }
            else {
                i = ind + groupString[j].size();
                j++;
            }
        }

        return j == groupString.size();
    }
};
// @lc code=end

