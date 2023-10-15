/*
 * @lc app=leetcode id=1944 lang=cpp
 *
 * [1944] Number of Visible People in a Queue
 */

// @lc code=start
/**
 * @lc app=leetcode id=1944 lang=cpp
 *
 * [1944] Number of Visible People in a Queue
 */

#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        stack<int> st;
        int n = heights.size();
        vector<int> result(n, 0);

        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && heights[i] >= heights[st.top()]) {
                st.pop();
                result[i]++;
            }

            if (!st.empty()) {
                result[i]++;
            }

            st.push(i);
        }

        return result;
    }
};

// @lc code=end

