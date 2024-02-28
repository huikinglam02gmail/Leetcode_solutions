/*
 * @lc app=leetcode id=2942 lang=csharp
 *
 * [2942] Find Words Containing Character
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public IList<int> FindWordsContaining(string[] words, char x) {
        List<int> result = new List<int>();
        for (int i = 0; i < words.Length; i++) {
            if (words[i].Contains(x)) {
                result.Add(i);
            }
        }
        return result;
    }
}

// @lc code=end

