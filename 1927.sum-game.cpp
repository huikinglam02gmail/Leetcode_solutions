/*
 * @lc app=leetcode id=1927 lang=cpp
 *
 * [1927] Sum Game
 */

// @lc code=start
#include <vector>
#include <map>
#include <tuple>
#include <string>

using std::make_tuple;
using std::string;
using std::tuple;

class Solution {
private:
    std::map<tuple<int, int, int>, bool> memo;

    bool dp(int diff, int lrDiff, int turn) {
        if (diff == 1) {
            return (turn == 0) ? true : !(-9 <= lrDiff && lrDiff <= 0);
        } else if (diff == -1) {
            return (turn == 0) ? true : !(0 <= lrDiff && lrDiff <= 9);
        } else if (memo.find(make_tuple(diff, lrDiff, turn)) == memo.end())
        {
            bool result = (turn == 0) ? false : true;

            if (diff > 0) 
            {
                for (int j = 0; j < 10; j++) 
                {
                    if (turn == 0) 
                    {
                        result = result || dp(diff - 1, lrDiff + j, 1 - turn);
                    } 
                    else 
                    {
                        result = result && dp(diff - 1, lrDiff + j, 1 - turn);
                    }
                }
            } else {
                for (int j = 0; j < 10; j++) {
                    if (turn == 0) {
                        result = result || dp(diff + 1, lrDiff - j, 1 - turn);
                    } else {
                        result = result && dp(diff + 1, lrDiff - j, 1 - turn);
                    }
                }
            }
            memo.insert({make_tuple(diff, lrDiff, turn), result});
        }
        return memo[make_tuple(diff, lrDiff, turn)];
    }

public:
    bool sumGame(std::string num) {
        int n = num.size();
        int l = 0;
        int r = 0;
        int leftSum = 0;
        int rightSum = 0;

        for (int i = 0; i < n; i++) {
            char c = num[i];
            if (i < n / 2) {
                if (c == '?') {
                    l++;
                } else {
                    leftSum += (c - '0');
                }
            } else {
                if (c == '?') {
                    r++;
                } else {
                    rightSum += (c - '0');
                }
            }
        }

        return dp(l - r, leftSum - rightSum, 0);
    }
};

// @lc code=end

