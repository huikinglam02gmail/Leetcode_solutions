/*
 * @lc app=leetcode id=1048 lang=cpp
 *
 * [1048] Longest String Chain
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
    This is a variation of the LIS problem. How to convert?
    The definition of predecessor:
    wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB
    LIS condition: nums[i] < nums[j]
    Longest string chain condition: s[i] is subsequence of s[j]
    important: len(s[i]) == len(s[j]) - 1 Otherwise no need consider
    To find the latter, we reuse function written in Leetcode 392 Is Subsequence
    and Leetcode 673 Number of Longest Increasing Subsequence    
    */

    bool isSubsequence(std::string s, std::string t) {
        int p1 = 0, p2 = 0;
        while (p1 < s.length() && p2 < t.length()) {
            if (s[p1] == t[p2]) {
                p1++;
            }
            p2++;
        }
        return p1 == s.length();
    }

    int longestStrChain(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end(), [](const std::string& a, const std::string& b) {
            return a.length() < b.length();
        });
        int n = words.size();
        std::vector<int> dp(n, 1);
        for (int j = n - 2; j >= 0; j--) {
            for (int k = j + 1; k < n; k++) {
                if (words[j].length() == words[k].length() - 1 && isSubsequence(words[j], words[k])) {
                    dp[j] = std::max(dp[j], dp[k] + 1);
                }
            }
        }
        int maxChain = 0;
        for (int chainLength : dp) {
            maxChain = std::max(maxChain, chainLength);
        }
        return maxChain;
    }
};
// @lc code=end

