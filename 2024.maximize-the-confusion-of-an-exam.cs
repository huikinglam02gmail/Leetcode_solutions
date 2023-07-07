/*
 * @lc app=leetcode id=2024 lang=csharp
 *
 * [2024] Maximize the Confusion of an Exam
 */

// @lc code=start
public class Solution {
    public int CharacterReplacement(string s, int k)
    {
        int left = 0;
        int right = 0;
        int[] occur = new int[26];
        int result = 0;
        while (right < s.Length)
        {
            if (right - left - occur.Max() <= k)
            {
                result = Math.Max(result, right - left);
                occur[s[right] - 'A'] += 1;
                right += 1;
            }
            else
            {
                occur[s[left] - 'A'] -= 1;
                left += 1;
            }
        }
        if (right - left - occur.Max() <= k)
        {
            result = Math.Max(result, right - left);
        }
        return result;
    }
    public int MaxConsecutiveAnswers(string answerKey, int k) {
        return CharacterReplacement(answerKey, k);
    }
}
// @lc code=end

