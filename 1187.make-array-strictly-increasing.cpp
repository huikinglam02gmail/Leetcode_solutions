/*
 * @lc app=leetcode id=1187 lang=cpp
 *
 * [1187] Make Array Strictly Increasing
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<tuple>
using std::tuple;
using std::unordered_map;
using std::vector;
class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) 
    {
        Arr2 = arr2;
        Array.Sort(Arr2);
        Arr1 = arr1;
        memo = new Dictionary<Tuple<int, int>, int>();
        int result = dp(0, -1);
        return result == Arr1.Length + 1 ? -1 : result;     
    }
private:
    unordered_map<tuple<int, int>, int> memo;
    vector<int> Arr1;
    vector<int> Arr2;
};
// @lc code=end

