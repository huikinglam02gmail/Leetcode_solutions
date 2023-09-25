/*
 * @lc app=leetcode id=1921 lang=cpp
 *
 * [1921] Eliminate Maximum Number of Monsters
 */

// @lc code=start
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        priority_queue<double, vector<double>, greater<double>> minHeap;
        int n = dist.size();
        
        for (int i = 0; i < n; i++) {
            minHeap.push((double)dist[i] / speed[i]);
        }
        
        int result = 0;
        
        while (!minHeap.empty() && (double)result < minHeap.top()) {
            minHeap.pop();
            result++;
        }
        
        return result;
    }
};

// @lc code=end

