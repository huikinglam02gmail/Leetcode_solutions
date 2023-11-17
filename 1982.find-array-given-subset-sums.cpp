/*
 * @lc app=leetcode id=1982 lang=cpp
 *
 * [1982] Find Array Given Subset Sums
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> recoverArray(int n, std::vector<int>& sums) {
        if (n == 0) {
            return std::vector<int>();
        } else {
            std::sort(sums.begin(), sums.end());
            int x = sums[1] - sums[0];
            std::vector<int> left, right;
            int indLeft = 0;

            for (int s : sums) {
                if (0 <= indLeft && indLeft < left.size() && s - x == left[indLeft]) {
                    right.push_back(s);
                    indLeft++;
                } else {
                    left.push_back(s);
                }
            }

            if (std::find(left.begin(), left.end(), 0) != left.end()) {
                std::vector<int> result = { x };
                auto recoveredArray = recoverArray(n - 1, left);
                result.insert(result.end(), recoveredArray.begin(), recoveredArray.end());
                return result;
            } else {
                std::vector<int> result = { -x };
                auto recoveredArray = recoverArray(n - 1, right);
                result.insert(result.end(), recoveredArray.begin(), recoveredArray.end());
                return result;
            }
        }
    }
};

// @lc code=end

