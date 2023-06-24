/*
 * @lc app=leetcode id=956 lang=cpp
 *
 * [956] Tallest Billboard
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<string>
#include<algorithm>
using std::max;
using std::string;
using std::to_string;
using std::unordered_map;
using std::vector;
class Solution {
private:
    vector<int> rods;
    unordered_map<string, int> cache;
    int DFS(int idx, int diff)
    {        
        if (idx == rods.size())
        {
            return diff == 0 ? 0 : -10000;
        }
        string key = to_string(idx) + "-" + to_string(diff);
        if (cache.find(key) == cache.end())
        {
            int skip = DFS(idx + 1, diff);
            int longSupport = DFS(idx + 1, diff + rods[idx]);
            int shortSupport = diff >= rods[idx] ? DFS(idx + 1, diff - rods[idx]) + rods[idx] : DFS(idx + 1, rods[idx] - diff) + diff; 
            cache.insert({key, max(skip, max(longSupport, shortSupport))});                     
        }
        return cache[key];
    }   
public:
    int tallestBillboard(vector<int>& rods) {
        this -> rods = rods;
        this -> cache = unordered_map<string, int>{};
        return DFS(0, 0);
    }
};
// @lc code=end

