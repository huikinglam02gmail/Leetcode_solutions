/*
 * @lc app=leetcode id=1647 lang=csharp
 *
 * [1647] Minimum Deletions to Make Character Frequencies Unique
 */

// @lc code=start
public class Solution {
    public int MinDeletions(string s) {
        int[] hashTable = new int[26];
        foreach (char c in s) {
            hashTable[c - 'a']++;
        }

        Array.Sort(hashTable, (a, b) => b.CompareTo(a));
        int result = 0;
        int maxFreq = hashTable[0];

        foreach (int count in hashTable) {
            if (count >= maxFreq) {
                result += count - maxFreq;
            } else {
                maxFreq = count;
            }

            if (maxFreq > 0) {
                maxFreq--;
            }
        }

        return result;
    }
}

// @lc code=end

