/*
 * @lc app=leetcode id=1187 lang=cpp
 *
 * [1187] Make Array Strictly Increasing
 */

// @lc code=start
#include<vector>
#include<map>
#include<tuple>
#include<algorithm>
using std::make_tuple;
using std::map;
using std::min;
using std::sort;
using std::tuple;
using std::upper_bound;
using std::vector;

class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) 
    {
        Arr2 = arr2;
        sort(Arr2.begin(), Arr2.end());
        Arr1 = arr1;
        int result = dp(0, -1);
        return result == Arr1.size() + 1 ? -1 : result;     
    }
private:
    map<tuple<int, int>, int> memo{};
    vector<int> Arr1;
    vector<int> Arr2;
    int dp(int i, int prev)
    {
        tuple<int, int> t = make_tuple(i, prev);

        if (i == Arr1.size())
        {
            return 0;
        }
        if (memo.find(t) == memo.end())
        {
            int result = Arr1.size() + 1;
            if (Arr1[i] > prev)
            {
                result = min(result, dp(i + 1, Arr1[i]));
            }
            int j = upper_bound(Arr2.begin(), Arr2.end(), prev) - Arr2.begin();
            if (j < Arr2.size())
            {
                result = min(result, 1 + dp(i + 1, Arr2[j]));
            }
            memo[t] = result;
        }
        return memo[t];
    }
};
// @lc code=end

