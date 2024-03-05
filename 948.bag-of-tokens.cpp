/*
 * @lc app=leetcode id=948 lang=cpp
 *
 * [948] Bag of Tokens
 */

// @lc code=start
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        if (tokens.empty()) return 0;
        int score = 0;
        deque<int> dq;
        sort(tokens.begin(), tokens.end());
        if (power >= tokens[0]) {
            for (int token : tokens) dq.push_back(token);
            while (dq.size() > 1) {
                if (power >= dq.front()) {
                    power -= dq.front();
                    dq.pop_front();
                    score++;
                } else {
                    power += dq.back();
                    dq.pop_back();
                    score--;
                }
            }
            if (power >= dq.front()) score++;
        }
        return score;
    }
};

// @lc code=end

