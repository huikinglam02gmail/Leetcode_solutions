/*
 * @lc app=leetcode id=2063 lang=cpp
 *
 * [2063] Vowels of All Substrings
 */

// @lc code=start
class Solution {
public:
    long long countVowels(string word) {
        long long last = 0;
        long long result = 0;
        int n = word.size();
        for (int i = 0; i < n; i++) {
            if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') {
                last += i + 1;
            }
            result += last;
        }
        return result;
    }
};
// @lc code=end

