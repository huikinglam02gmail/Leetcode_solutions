/*
 * @lc app=leetcode id=1769 lang=cpp
 *
 * [1769] Minimum Number of Operations to Move All Balls to Each Box
 */

// @lc code=start
#include<vector>
#include<queue>
#include<string>
using std::queue;
using std::string;
using std::vector;
class Solution {
public:
    vector<int> minOperations(string boxes) {
        queue<int> dq {};
        int leftS = 0, rightS = 0, n = boxes.size(), leftCount = 0;
        vector<int> result {};

        for (int i = 0; i < n; i++) {
            if (boxes[i] == '1') {
                dq.push(i);
                rightS += i;
            }
        }

        for (int j = 0; j < n; j++) {
            if (dq.size() > 0 && j == dq.front()) {
                leftS += dq.front();
                dq.pop();
                rightS -= j;
                leftCount++;
            }

            result.push_back(leftCount * j - leftS + rightS - dq.size() * j);
        }

        return result;        
    }
};
// @lc code=end

