/*
 * @lc app=leetcode id=2801 lang=csharp
 *
 * [2801] Count Stepping Numbers in Range
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007;
    private Dictionary<Tuple<int, bool, int, string>, long> cache;
    
    public long CountSteppingNumbers(string low, string high) {
        cache = new Dictionary<Tuple<int, bool, int, string>, long>();
        return Convert.ToInt32((Count(high) - Count(MinusOne(low)) + MOD) % MOD);
    }

    private long DP(int i, bool tight, int lastDigit, string num) 
    {
        Tuple<int, bool, int, string> t = new Tuple<int, bool, int, string>(i, tight, lastDigit, num);
        if (i == num.Length) {
            return 1;
        }
        if (!cache.ContainsKey(t)) 
        {
            int maxDigit = tight ? num[i] - '0' : 9;
            long ans = 0;
            
            for (int d = 0; d <= maxDigit; d++) {
                bool nxtTight = tight && d == maxDigit;
                
                if (lastDigit == -1) {
                    int d1 = (d == 0) ? -1 : d;
                    ans += DP(i + 1, nxtTight, d1, num);
                    ans %= MOD;
                }
                else if (Math.Abs(lastDigit - d) == 1) {
                    ans += DP(i + 1, nxtTight, d, num);
                    ans %= MOD;
                }
            }
            cache.Add(t, ans);
        }
        return cache[t];
    }
    private long Count(string num) {
        return DP(0, true, -1, num);
    }
    
    private string MinusOne(string s) {
        char[] arr = s.ToCharArray();
        int carry = 1;
        for (int i = arr.Length - 1; i >= 0; i--) {
            arr[i] -= (char)carry;
            carry = 0;
            if (arr[i] < '0') {
                arr[i] += (char)10;
                carry++;
            }
        }
        int idx = 0;
        while (idx < arr.Length && arr[idx] == '0') {
            idx++;
        }
        return new string(arr).Substring(idx);
    }
}

// @lc code=end

