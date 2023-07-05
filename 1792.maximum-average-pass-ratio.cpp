/*
 * @lc app=leetcode id=1792 lang=cpp
 *
 * [1792] Maximum Average Pass Ratio
 */

// @lc code=start
#include<vector>
#include<queue>
#include<tuple>
using std::get;
using std::make_tuple;
using std::priority_queue;
using std::tuple;
using std::vector;
class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        priority_queue<tuple<double, int, int>> pq{};
        int n = classes.size();
        for (vector<int> cl : classes) 
        {
            pq.push(make_tuple(- (double)cl[0] / (double)cl[1] + (double)(cl[0] + 1) / (double)(cl[1] + 1), cl[0], cl[1]));
        }
        for (int j = extraStudents; j > 0; j--)
        {
            tuple<double, int, int> cl = pq.top();
            pq.pop();
            pq.push(make_tuple(-(double)(get<1>(cl) + 1) / (double)(get<2>(cl) + 1) + (double)(get<1>(cl) + 2) / (double)(get<2>(cl) + 2), get<1>(cl) + 1, get<2>(cl) + 1));
        }

        double result = 0;
        while (!pq.empty())
        {
            tuple<double, int, int> cl = pq.top();
            pq.pop();
            result += (double)get<1>(cl) / (double)get<2>(cl);
        }
        return result / (double)n;        
    }
};
// @lc code=end

