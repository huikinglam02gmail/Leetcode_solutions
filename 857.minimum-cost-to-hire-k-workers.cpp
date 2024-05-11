/*
 * @lc app=leetcode id=857 lang=cpp
 *
 * [857] Minimum Cost to Hire K Workers
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        vector<pair<double, int>> ratio;
        for (int i = 0; i < quality.size(); ++i) {
            ratio.push_back({(double)wage[i] / quality[i], quality[i]});
        }
        sort(ratio.begin(), ratio.end());

        priority_queue<int> heap;
        int qSum = 0;
        double result = numeric_limits<double>::infinity();

        for (auto& worker : ratio) {
            qSum += worker.second;
            heap.push(worker.second);

            if (heap.size() > k) {
                qSum -= heap.top();
                heap.pop();
            }

            if (heap.size() == k) {
                result = min(result, qSum * worker.first);
            }
        }

        return result;
    }
};

// @lc code=end

