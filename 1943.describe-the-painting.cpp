/*
 * @lc app=leetcode id=1943 lang=cpp
 *
 * [1943] Describe the Painting
 */

// @lc code=start
/**
 * @lc app=leetcode id=1943 lang=cpp
 *
 * [1943] Describe the Painting
 */

#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

class Solution {
public:
    void endOldSegment(long long i, long long totalColor) {
        if (!result.empty()) {
            result.back()[1] = i;
            result.back()[2] = totalColor;
        }
    }

    void addNewSegment(long long i) {
        result.push_back({i, -1LL, -1LL});
    }

    vector<vector<long long>> splitPainting(vector<vector<int>>& segments) {
        priority_queue<vector<long long>, vector<vector<long long>>, greater<vector<long long>>> exit; // Use a priority queue for exit information
        long long cumu = 0LL;
        int segmentPtr = 0;

        sort(segments.begin(), segments.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        int limit = 0;
        for (const vector<int>& segment : segments) {
            limit = max(limit, segment[1]);
        }

        for (int i = 1; i <= limit; i++) {
            int countSameEnd = 0;
            while (!exit.empty() && exit.top()[0] == i) {
                vector<long long> exitSegment = exit.top();
                exit.pop();
                countSameEnd++;

                if (countSameEnd == 1) {
                    endOldSegment(i, cumu);
                    addNewSegment(i);
                }

                cumu -= exitSegment[1];
            }

            int countSameStart = 0;
            while (segmentPtr < segments.size() && segments[segmentPtr][0] == i) {
                vector<int> segment = segments[segmentPtr];
                exit.push({static_cast<long long>(segment[1]), static_cast<long long>(segment[2])});
                countSameStart++;

                if (countSameStart == 1) {
                    if (cumu > 0LL && !result.empty() && result.back()[0] != i) {
                        endOldSegment(i, cumu);
                        addNewSegment(i);
                    } else if (!result.empty()) {
                        result.back()[0] = i;
                    } else {
                        addNewSegment(i);
                    }
                }
                cumu += static_cast<long long>(segment[2]);
                segmentPtr++;
            }
        }

        result.pop_back();

        return result;
    }
private:
    vector<vector<long long>> result{};
};

// @lc code=end

