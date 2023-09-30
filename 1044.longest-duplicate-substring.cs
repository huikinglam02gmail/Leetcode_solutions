/*
 * @lc app=leetcode id=1044 lang=csharp
 *
 * [1044] Longest Duplicate Substring
 */

// @lc code=start
public class Solution {
    private long basis = 29;
    private long MOD = 1 << 31 - 1;
    private List<long> lookup;
    private string s;

    private long RollingHash(int i, int size, long seed) {
        long h = seed;
        if (i == 0) 
        {
            for (int j = 0; j < size; j++) 
            {
                h *= basis;
                h += s[i + j] - 'a';
                h %= MOD;
            }
        } 
        else 
        {
            h -= (s[i - 1] - 'a') * lookup[size - 1];
            while (h < 0)
            {
                h += MOD;
            } 
            h *= basis;
            h += s[i + size - 1] - 'a';
            h %= MOD;
        }
        return h;
    }

    private int[] FoundSubString(int size) 
    {
        Dictionary<long, int> seen = new Dictionary<long, int>();
        int[] result = new int[2] { 0, -1 };
        long h = 0;
        for (int i = 0; i < s.Length - size + 1; i++) {
            h = RollingHash(i, size, h);
            if (!seen.ContainsKey(h)) 
            {
                seen[h] = i;
            } 
            else 
            {
                int j = seen[h];
                if (s.Substring(i, size) == s.Substring(j, size)) 
                {
                    return new int[2] { 1, j };
                }
            }
        }
        return result;
    }

    public string LongestDupSubstring(string s) 
    {
        this.s = s;
        int n = s.Length;
        if (n == 2) {
            if (s[0] == s[1]) {
                return s[0].ToString();
            }
            return "";
        }

        long seed = 1;
        lookup = new List<long>();
        for (int i = 0; i < n; i++) 
        {
            lookup.Add(seed);
            seed *= basis;
            seed %= MOD;
        }

        int left = 1, right = s.Length, startIndex = -1;

        while (left < right) 
        {
            int mid = left + (right - left) / 2;
            int[] result = FoundSubString(mid);
            int exist = result[0];
            int j = result[1];

            if (exist == 1) 
            {
                left = mid + 1;
                startIndex = j;
            } 
            else 
            {
                right = mid;
            }
        }

        if (startIndex != -1) 
        {
            return s.Substring(startIndex, left - 1);
        } 
        else 
        {
            return "";
        }
    }
}

// @lc code=end

