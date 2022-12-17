/*
 * @lc app=leetcode id=1542 lang=csharp
 *
 * [1542] Find Longest Awesome Substring
 */

// @lc code=start
public class Solution 
{
    public int LongestAwesome(string s) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        HashSet<int> palindromes = new HashSet<int>();
        int current = 0;
        int result = 0;

        hashTable.Add(0, -1);
        palindromes.Add(0);
        for (int i = 0; i < 10; i++)
        {
            palindromes.Add(1 << i);
        }

        for (int i = 0; i < s.Length; i++)
        {
            current ^= (1 << ((int) s[i] - (int) '0'));
            if (!hashTable.ContainsKey(current))
            {
                hashTable[current] = i;
            }
            foreach (int item in palindromes)
            {
                if (hashTable.ContainsKey(current ^ item))
                {
                    result = Math.Max(result, i - hashTable[current ^ item]);
                }
            }
        }
        return result;
    }
}
// @lc code=end
