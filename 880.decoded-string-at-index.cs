/*
 * @lc app=leetcode id=880 lang=csharp
 *
 * [880] Decoded String at Index
 */

// @lc code=start
public class Solution {
    public string DecodeAtIndex(string s, int k) {
        long size = 0;
        long kLong = (long)k;
        
        foreach (char c in s) {
            if (char.IsLetter(c)) {
                size++;
            }
            else {
                size *= long.Parse(c.ToString());
            }
        }
        
        foreach (char c in s.Reverse()) {
            kLong %= size;
            
            if (kLong == 0 && char.IsLetter(c)) {
                return c.ToString();
            }
            
            if (char.IsLetter(c)) {
                size--;
            }
            else {
                size /= long.Parse(c.ToString());
            }
        }
        
        return string.Empty; // Return empty string if no result is found.
    }
}

// @lc code=end

