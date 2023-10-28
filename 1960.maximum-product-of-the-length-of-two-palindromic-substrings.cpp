/*
 * @lc app=leetcode id=1960 lang=cpp
 *
 * [1960] Maximum Product of the Length of Two Palindromic Substrings
 */

// @lc code=start
#include<vector>
#include<string>
#include<algorithm>

using std::max;
using std::string;
using std::vector;

class Solution {
public:
    vector<int> Manacher(string s) {
        int n = s.size();
        vector<int> LPS(n, 0);
        int C = 0; // center
        int R = 0; // rightmost palindrome
        int j;

        for (int i = 0; i < n; i++) {
            if (i < C + R) { // if there's an overlap
                j = LPS[C - (i - C)]; // reflect

                if (j < C + R - i) { // case A
                    LPS[i] = j;
                    continue;
                }
                else if (j > C + R - i) { // case B
                    LPS[i] = C + R - i;
                    continue;
                }
                // case C: do nothing
            }
            else { // no overlap
                j = 0;
            }

            while (i - j > 0 && i + j < n - 1 && s[i - j - 1] == s[i + j + 1]) {
                j++;
            }

            LPS[i] = j;

            if (i + j > C + R) {
                C = i;
                R = j;
            }
        }
        return LPS;
    }

    long long maxProduct(std::string s) {
        int n = s.length();
        vector<int> LPS = Manacher(s);
        vector<int> prefix(n, 0);
        vector<int> suffix(n, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + LPS[i]] = max(prefix[i + LPS[i]], 2 * LPS[i] + 1);
            suffix[i - LPS[i]] = max(suffix[i - LPS[i]], 2 * LPS[i] + 1);
        }

        for (int i = n - 2; i >= 0; i--) {
            prefix[i] = max(prefix[i], prefix[i + 1] - 2);
        }

        for (int i = 1; i < n; i++) {
            suffix[i] = max(suffix[i], suffix[i - 1] - 2);
        }

        std::vector<int> prefixMax(n, 0);
        std::vector<int> suffixMax(n, 0);
        int cur = 0;

        for (int i = 0; i < n; i++) {
            cur = max(cur, prefix[i]);
            prefixMax[i] = cur;
        }

        cur = 0;
        for (int i = n - 1; i >= 0; i--) {
            cur = max(cur, suffix[i]);
            suffixMax[i] = cur;
        }

        long long result = 0;

        for (int i = 0; i < n - 1; i++) {
            result = max(result, static_cast<long long>(prefixMax[i]) * static_cast<long long>(suffixMax[i + 1]));
        }

        return result;
    }

};
// @lc code=end

