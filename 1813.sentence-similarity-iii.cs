/*
 * @lc app=leetcode id=1813 lang=csharp
 *
 * [1813] Sentence Similarity III
 */

// @lc code=start
public class Solution {
    private bool Similar(List<string> s1Split, List<string> s2Split) {
        int i = 0, j = 0, numSkip = 0;
        while (i < s1Split.Count && j < s2Split.Count) {
            if (s2Split[j] != s1Split[i]) {
                numSkip++;
                if (numSkip > 1)
                    return false;
                while (i < s1Split.Count && s1Split[i] != s2Split[j])
                    i++;
            } else {
                i++;
                j++;
            }
        }
        return (j == s2Split.Count && i == s1Split.Count && numSkip <= 1) || (i < s1Split.Count && numSkip == 0);
    }

    public bool AreSentencesSimilar(string sentence1, string sentence2) {
        var s1Split = sentence1.Split(' ').ToList();
        var s2Split = sentence2.Split(' ').ToList();
        if (s1Split.Count < s2Split.Count) {
            var temp = s1Split;
            s1Split = s2Split;
            s2Split = temp;
        }
        return Similar(s1Split, s2Split) || Similar(s1Split.AsEnumerable().Reverse().ToList(), s2Split.AsEnumerable().Reverse().ToList());
    }
}

// @lc code=end

