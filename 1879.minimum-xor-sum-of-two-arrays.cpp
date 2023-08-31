/*
 * @lc app=leetcode id=1879 lang=cpp
 *
 * [1879] Minimum XOR Sum of Two Arrays
 */

// @lc code=start
#include <vector>
#include <map>

using namespace std;

class Solution {
private:
    vector<int> nums1;
    vector<int> nums2;
    map<pair<int, int>, int> memo;

public:
    int minimumXORSum(vector<int>& nums1, vector<int>& nums2) {
        this->nums1 = nums1;
        this->nums2 = nums2;
        return DP(0, 0);
    }

    int DP(int i, int mask) {
        if (i == nums1.size())
            return 0;

        auto state = make_pair(i, mask);
        if (memo.find(state) != memo.end())
            return memo[state];

        int result = INT_MAX;
        for (int j = 0; j < nums1.size(); j++) {
            if ((mask & (1 << j)) == 0) {
                result = min(result, (nums1[i] ^ nums2[j]) + DP(i + 1, mask ^ (1 << j)));
            }
        }

        memo[state] = result;
        return result;
    }
};
// @lc code=end

