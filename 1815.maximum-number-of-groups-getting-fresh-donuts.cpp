/*
 * @lc app=leetcode id=1815 lang=cpp
 *
 * [1815] Maximum Number of Groups Getting Fresh Donuts
 */

// @lc code=start
#include<map>
#include<string>
#include<vector>
using std::pair;
using std::string;
using std::map;
using std::vector;
class Solution {
private:
    map<pair<string, int>, int> memo {};
    int dp(const string& state, int remainder, int batchSize) {
        if (state.length() == 0) return 0;
        auto key = std::make_pair(state, remainder);
        if (memo.find(key) != memo.end()) {
            return memo[key];
        }

        int result = (remainder == 0) ? 1 : 0;
        int extra = 0;

        for (int i = 0; i < state.length(); i++) {
            if (i == 0 || state[i] != state[i - 1]) {
                int nextRemainder = (remainder + (state[i] - '0')) % batchSize;
                extra = std::max(extra, dp(state.substr(0, i) + state.substr(i + 1), nextRemainder, batchSize));
            }
        }

        memo[key] = result + extra;
        return memo[key];
    }    
public:
    int maxHappyGroups(int batchSize, vector<int>& groups) {
        vector<int> counts(batchSize);
        for (int group : groups) {
            counts[group % batchSize]++;
        }
        int result = counts[0];
        for (int i = 1; i <= batchSize / 2; i++) {
            int toReduce = (2 * i != batchSize) ? std::min(counts[i], counts[batchSize - i]) : counts[i] / 2;
            counts[i] -= toReduce;
            counts[batchSize - i] -= toReduce;
            result += toReduce;
        }

        string initialState = "";
        for (int i = 1; i < batchSize; i++) {
            initialState += string(counts[i], static_cast<char>('0' + i));
        }
        return result + dp(initialState, 0, batchSize);
    }
};
// @lc code=end

