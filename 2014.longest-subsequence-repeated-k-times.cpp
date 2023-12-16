/*
 * @lc app=leetcode id=2014 lang=cpp
 *
 * [2014] Longest Subsequence Repeated k Times
 */

// @lc code=start
#include <vector>
#include <map>
#include <unordered_set>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
private:
    map<pair<int, string>, unordered_set<string>> dp;

    bool IsSubsequence(const string& s, const string& t) {
        int p1 = 0, p2 = 0;
        while (p1 < s.length() && p2 < t.length()) {
            if (s[p1] == t[p2]) {
                p1++;
            }
            p2++;
        }
        return p1 == s.length();
    }

    unordered_set<string> GenerateCandidates(int remainCharacters, const string& availableCharacters) {
        pair<int, string> t = { remainCharacters, availableCharacters };
        if (dp.find(t) == dp.end()) {
            unordered_set<string> result;
            if (remainCharacters > 0) {
                for (int i = 0; i < availableCharacters.length(); i++) {
                    if (i > 0 && availableCharacters[i] == availableCharacters[i - 1]) continue;
                    auto furtherSearchSet = GenerateCandidates(remainCharacters - 1, availableCharacters.substr(0, i) + availableCharacters.substr(i + 1));
                    for (const auto& s : furtherSearchSet) {
                        result.insert(availableCharacters[i] + s);
                    }
                }
            }
            else
                result.insert(string {""});
            dp[t] = result;
        }
        return dp[t];
    }

public:
    string longestSubsequenceRepeatedK(const string& s, int k) {
        vector<int> occur(26, 0);
        int n = s.length();

        for (char c : s) {
            occur[c - 'a']++;
        }

        string startingString = "";
        for (int i = 25; i >= 0; i--) {
            startingString += string(occur[i] / k, static_cast<char>(i + 'a'));
        }

        dp.clear();

        for (int i = min(n / k, static_cast<int>(startingString.length())); i > 0; i--) {
            unordered_set<string> candidatesSet {GenerateCandidates(i, startingString)};
            vector<string> candidates (candidatesSet.begin(), candidatesSet.end());
            sort(candidates.begin(), candidates.end(), greater<string>());

            for (const auto& cand : candidates) {
                string subseq = "";
                for (int j = 0; j < k; ++j) subseq += cand;
                if (IsSubsequence(subseq, s)) {
                    return cand;
                }
            }
        }

        return "";
    }
};


// @lc code=end

