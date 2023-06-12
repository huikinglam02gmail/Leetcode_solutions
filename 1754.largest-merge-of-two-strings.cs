/*
 * @lc app=leetcode id=1754 lang=csharp
 *
 * [1754] Largest Merge Of Two Strings
 */

// @lc code=start
public class Solution {
    public string LargestMerge(string word1, string word2) {
        int i = 0;
        int j = 0;
        int n1 = word1.Length;
        int n2 = word2.Length;

        string dfs(int i, int j)
        {
            if (i == n1)
                return word2.Substring(j);
            else if (j == n2)
                return word1.Substring(i);
            else if (string.CompareOrdinal(word1.Substring(i), word2.Substring(j)) >= 0)
                return word1[i] + dfs(i + 1, j);
            else
                return word2[j] + dfs(i, j + 1);
        }

        return dfs(0, 0);
    }
}
// @lc code=end

