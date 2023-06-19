/*
 * @lc app=leetcode id=16 lang=cpp
 *
 * [16] 3Sum Closest
 */

// @lc code=start
#include <vector>
#include<algorithm>
using std::abs;
using std::sort;
using std::vector;
class Solution {
private:
    int closerToTarget(const int x1, const int x2, const int target)
    {
        return abs(x1 - target) < abs(x2 - target) ? x1 : x2;
    }
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int result = 100000;
        int n = nums.size();
        
        for (int i = 0; i < n - 2; i++) {
            int S1 = nums[i] + nums[i + 1] + nums[i + 2];
            int S2 = nums[i] + nums[n - 2] + nums[n - 1];
            result = closerToTarget(result, S1, target);
            result = closerToTarget(result, S2, target);

            if (S1 <= target && target <= S2) {
                int left = i + 1;
                int right = n - 1;
                
                while (left < right) {
                    int S = nums[i] + nums[left] + nums[right];
                    result = closerToTarget(result, S, target);
                    if (S == target) {
                        return target;
                    }
                    else if (S < target) {
                        left++;
                    }
                    else {
                        right--;
                    }
                }
            }
        }        
        return result;
    }
};
// @lc code=end

