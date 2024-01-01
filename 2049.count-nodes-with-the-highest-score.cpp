/*
 * @lc app=leetcode id=2049 lang=cpp
 *
 * [2049] Count Nodes With the Highest Score
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>
#include <unordered_map>
#include <climits>

using namespace std;

class Solution {
public:
    int countHighestScoreNodes(vector<int>& parents) {
        int n = parents.size();
        vector<unordered_set<int>> children(n);
        vector<int> offsprings(n, 0);

        for (int i = 0; i < n; ++i) {
            if (parents[i] >= 0) {
                children[parents[i]].insert(i);
                offsprings[parents[i]]++;
            }
        }

        vector<int> subtreeSize(n, 1);
        queue<int> dq;
        for (int i = 0; i < n; ++i) {
            if (offsprings[i] == 0) {
                dq.push(i);
            }
        }

        while (!dq.empty()) {
            int node = dq.front();
            dq.pop();

            if (parents[node] >= 0) {
                offsprings[parents[node]]--;
                subtreeSize[parents[node]] += subtreeSize[node];

                if (offsprings[parents[node]] == 0) {
                    dq.push(parents[node]);
                }
            }
        }

        unordered_map<long, int> counts;
        long maxScore = 0;
        for (int i = 0; i < n; ++i) {
            long score = 1;

            for (int child : children[i]) {
                score *= subtreeSize[child];
            }

            if (parents[i] >= 0) {
                score *= n - subtreeSize[i];
            }

            counts[score] = counts.count(score) ? counts[score] + 1 : 1;
            maxScore = max(maxScore, score);
        }

        return counts[maxScore];
    }
};

// @lc code=end

