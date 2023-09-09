/*
 * @lc app=leetcode id=1889 lang=cpp
 *
 * [1889] Minimum Space Wasted From Packaging
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int minWastedSpace(std::vector<int>& packages, std::vector<std::vector<int>>& boxes) {
        const long long MOD = 1000000007;
        std::sort(packages.begin(), packages.end());
        std::vector<long long> prefix(packages.size() + 1, 0);

        for (int i = 0; i < packages.size(); i++) {
            prefix[i + 1] = prefix[i] + packages[i];
        }

        long long result = LLONG_MAX;
        for (const std::vector<int>& box : boxes) {
            std::vector<int> boxCopy = box;
            std::sort(boxCopy.begin(), boxCopy.end());
            long long current = 0;
            int prev = 0;

            for (int j : boxCopy) {
                int ind = std::upper_bound(packages.begin(), packages.end(), j) - packages.begin();
                current += (ind - prev) * static_cast<long long>(j) - (prefix[ind] - prefix[prev]);
                prev = ind;
            }

            if (prev == packages.size()) {
                result = std::min(result, current);
            }
        }

        return result != LLONG_MAX ? static_cast<int>(result % MOD) : -1;
    }
};

// @lc code=end

