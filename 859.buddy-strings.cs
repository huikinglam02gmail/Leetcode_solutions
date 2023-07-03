/*
 * @lc app=leetcode id=859 lang=csharp
 *
 * [859] Buddy Strings
 */

// @lc code=start
public class Solution {
    /*
    Two cases to be a pair of buddy strings:
    identical, at least one character appears twice
    Two mismatches, corresponding positions    
    */

    public bool BuddyStrings(string s, string goal) {
        if (s.Length == goal.Length) {
            var hashTable = new Dictionary<char, int>();
            var mismatch = new List<char[]>();
            for (int i = 0; i < s.Length; i++) {
                if (!hashTable.ContainsKey(s[i])) {
                    hashTable[s[i]] = 0;
                }
                hashTable[s[i]]++;
                if (s[i] != goal[i]) {
                    mismatch.Add(new char[] { s[i], goal[i] });
                }
            }
            switch(mismatch.Count)
            {
                case 0: return hashTable.Values.Max() > 1;
                case 2: return mismatch[0][0] == mismatch[1][1] && mismatch[0][1] == mismatch[1][0];
            }
        }
        return false;
    }
}

// @lc code=end

