/*
 * @lc app=leetcode id=2785 lang=csharp
 *
 * [2785] Sort Vowels in a String
 */

// @lc code=start
public class Solution {
    public string SortVowels(string s) {
        List<char> vowels = new List<char>();
        List<int> indices = new List<int>();
        char[] result = new char[s.Length];

        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            if ("aeiouAEIOU".Contains(c)) {
                vowels.Add(c);
                indices.Add(i);
            }
            result[i] = c;
        }

        vowels.Sort();
        for (int i = 0; i < vowels.Count; i++) {
            result[indices[i]] = vowels[i];
        }

        return new string(result);
    }
}

// @lc code=end

