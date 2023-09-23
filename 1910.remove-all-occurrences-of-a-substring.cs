/*
 * @lc app=leetcode id=1910 lang=csharp
 *
 * [1910] Remove All Occurrences of a Substring
 */

// @lc code=start
public class Solution {
    public string RemoveOccurrences(string s, string part) {
        var result = new List<char>();
        var n = part.Length;
        
        foreach (var c in s) {
            result.Add(c);
            if (result.Count >= n && new string(result.GetRange(result.Count - n, n).ToArray()) == part) {
                for (int j = 0; j < n; j++) {
                    result.RemoveAt(result.Count - 1);
                }
            }
        }
        
        return new string(result.ToArray());
    }
}

// @lc code=end

