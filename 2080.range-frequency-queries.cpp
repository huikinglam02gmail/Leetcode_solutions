/*
 * @lc app=leetcode id=2080 lang=cpp
 *
 * [2080] Range Frequency Queries
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class RangeFreqQuery {
private:
    unordered_map<int, vector<int>> appear;

public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0; i < arr.size(); i++) {
            appear[arr[i]].push_back(i);
        }
    }

    int query(int left, int right, int value) {
        if (appear.find(value) == appear.end()) {
            return 0;
        } else {
            return upper_bound(appear[value].begin(), appear[value].end(), right) - lower_bound(appear[value].begin(), appear[value].end(), left);
        }
    }
};


/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery* obj = new RangeFreqQuery(arr);
 * int param_1 = obj->query(left,right,value);
 */
// @lc code=end

