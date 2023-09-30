/*
 * @lc app=leetcode id=1044 lang=cpp
 *
 * [1044] Longest Duplicate Substring
 */

// @lc code=start
#include <string>
#include <vector>
#include <unordered_map>

class Solution {
private:
    const long long basis = 29;
    const long long MOD = (1LL << 31) - 1;
    std::vector<long long> lookup;
    std::string s;

    long long RollingHash(int i, int size, long long seed) {
        long long h = seed;
        if (i == 0) {
            for (int j = 0; j < size; j++) {
                h = (h * basis + (s[i + j] - 'a')) % MOD;
            }
        } else {
            h = (h - (s[i - 1] - 'a') * lookup[size - 1]) % MOD;
            while (h < 0) {
                h += MOD;
            }
            h = (h * basis + (s[i + size - 1] - 'a')) % MOD;
        }
        return h;
    }

    std::vector<int> FoundSubString(int size) {
        std::unordered_map<long long, int> seen;
        std::vector<int> result(2, 0);
        long long h = 0;
        for (int i = 0; i < s.length() - size + 1; i++) {
            h = RollingHash(i, size, h);
            if (seen.find(h) == seen.end()) {
                seen[h] = i;
            } else {
                int j = seen[h];
                if (s.substr(i, size) == s.substr(j, size)) {
                    return std::vector<int>{1, j};
                }
            }
        }
        return result;
    }

public:
    std::string longestDupSubstring(std::string s) {
        this->s = s;
        int n = s.length();
        if (n == 2) {
            if (s[0] == s[1]) {
                return s.substr(0, 1);
            }
            return "";
        }

        long long seed = 1;
        lookup.clear();
        for (int i = 0; i < n; i++) {
            lookup.push_back(seed);
            seed = (seed * basis) % MOD;
        }

        int left = 1, right = s.length(), startIndex = -1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            std::vector<int> result = FoundSubString(mid);
            int exist = result[0];
            int j = result[1];

            if (exist == 1) {
                left = mid + 1;
                startIndex = j;
            } else {
                right = mid;
            }
        }

        if (startIndex != -1) {
            return s.substr(startIndex, left - 1);
        } else {
            return "";
        }
    }
};
// @lc code=end

