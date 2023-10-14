/*
 * @lc app=leetcode id=503 lang=cpp
 *
 * [503] Next Greater Element II
 */

// @lc code=start
/*
 * @lc app=leetcode id=503 lang=cpp
 *
 * [503] Next Greater Element II
 */

#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> nextGreater(2 * n, -1);
        stack<int> stack;
        vector<int> nums2(2 * n);

        for (int i = 0; i < n; i++) {
            nums2[i] = nums[i];
            nums2[i + n] = nums[i];
        }

        for (int i = 0; i < 2 * n; i++) {
            while (!stack.empty() && nums2[i] > nums2[stack.top()]) {
                nextGreater[stack.top()] = nums2[i];
                stack.pop();
            }
            stack.push(i);
        }

        vector<int> result(nextGreater.begin(), nextGreater.begin() + n);
        return result;
    }
};

// @lc code=end

