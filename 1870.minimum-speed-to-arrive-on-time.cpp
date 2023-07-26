/*
 * @lc app=leetcode id=1870 lang=cpp
 *
 * [1870] Minimum Speed to Arrive on Time
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<int> dist;
    double hour;

    double TimeToReach(int speed) {
        double result = 0;
        for (int i = 0; i < dist.size() - 1; i++) {
            result += (dist[i] + speed - 1) / speed;
        }
        return (double)result + static_cast<double>(dist.back()) / static_cast<double>(speed);
    }

public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        this->dist = dist;
        this->hour = hour;
        int maxDist = *max_element(dist.begin(), dist.end());

        int l = 1, r = maxDist * 100 + 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (TimeToReach(mid) > hour) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l == maxDist * 100 + 1 ? -1 : l;
    }
};

// @lc code=end

