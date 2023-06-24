/*
 * @lc app=leetcode id=1776 lang=cpp
 *
 * [1776] Car Fleet II
 */

// @lc code=start
#include<vector>
#include<stack>
using std::stack;
using std::vector;
class Solution {
public:
    vector<double> getCollisionTimes(vector<vector<int>>& cars) {
        stack<vector<double>> stack {};
        vector<double> result = {};
        result.resize(cars.size(), (double)(-1));
        for (int i = cars.size() - 1; i >= 0; i--)
        {
            double pos = (double)cars[i][0];
            double speed = (double)cars[i][1];

            while (stack.size() > 0 && (speed <= stack.top()[1] || (stack.top()[0] - pos) / (speed - stack.top()[1]) >= stack.top()[2]))
            {
                stack.pop();
            }

            if (stack.size() == 0)
            {
                stack.push(vector<double> { pos, speed, HUGE_VAL });
            }
            else
            {
                double collisionTime = (stack.top()[0] - pos) / (speed - stack.top()[1]);
                stack.push(vector<double> { pos, speed, collisionTime });
                result[i] = collisionTime;
            }
        }
        
        return result;
    }
};
// @lc code=end

