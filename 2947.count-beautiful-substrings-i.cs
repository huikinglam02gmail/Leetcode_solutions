/*
 * @lc app=leetcode id=2947 lang=csharp
 *
 * [2947] Count Beautiful Substrings I
 */

// @lc code=start
public class Solution {
    public int BeautifulSubstrings(string s, int k) {
        int N = s.Length;
        HashSet<char> vowels = new HashSet<char> {'a', 'e', 'i', 'o', 'u'};
        int ans = 0;

        for (int i = 0; i < N; i++) {
            int c = 0, v = 0;

            for (int j = i; j < N; j++) {
                if (vowels.Contains(s[j])) {
                    v++;
                } else {
                    c++;
                }

                ans += (c == v  && v * c % k == 0) ? 1 : 0;
            }
        }

        return ans;
    }
}

// @lc code=end

