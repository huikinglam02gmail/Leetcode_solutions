/*
 * @lc app=leetcode id=2024 lang=cpp
 *
 * [2024] Maximize the Confusion of an Exam
 */

// @lc code=start
#include<string>
#include<vector>
#include<algorithm>
using std::max;
using std::max_element;
using std::string;
using std ::vector;
class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int right = 0;
        vector<int> occur(26, 0);
        int result = 0;
        while (right < s.size())
        {
            if (right - left - *max_element(occur.begin(), occur.end()) <= k)
            {
                result = max(result, right - left);
                occur[s[right] - 'A'] += 1;
                right += 1;
            }
            else
            {
                occur[s[left] - 'A'] -= 1;
                left += 1;
            }
        }
        if (right - left - *max_element(occur.begin(), occur.end()) <= k)
        {
            result = max(result, right - left);
        }
        return result;        
    }

    int maxConsecutiveAnswers(string answerKey, int k) {
        return characterReplacement(answerKey, k);
    }
};
// @lc code=end

