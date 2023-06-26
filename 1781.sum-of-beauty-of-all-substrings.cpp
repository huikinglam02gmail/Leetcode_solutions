/*
 * @lc app=leetcode id=1781 lang=cpp
 *
 * [1781] Sum of Beauty of All Substrings
 */

// @lc code=start
#include<string>
#include<vector>
#include<algorithm>
#include<iterator>
using std::back_inserter;
using std::copy_if;
using std::minmax_element;
using std::string;
using std::vector;
class Solution {
public:
    int beautySum(string s) {
        int result = 0;
        int n = s.size();
        auto positive = [](int i) { return i > 0; };
        vector<int> temp;
        for (int i = 0; i < n; i++)
        {
            vector<int> count(26, 0);
            for (int j = i; j < n; j++)
            {
                count[s[j] - 'a']++;
                temp.clear();
                copy_if(count.begin(), count.end(), back_inserter(temp), positive);
                auto res = minmax_element(temp.begin(), temp.end());
                result += *res.second - *res.first;
            }
        }
        return result;        
    }
};
// @lc code=end

