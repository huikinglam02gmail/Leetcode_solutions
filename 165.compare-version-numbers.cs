/*
 * @lc app=leetcode id=165 lang=csharp
 *
 * [165] Compare Version Numbers
 */

// @lc code=start
using System;

public class Solution {
    public string[] TrimLeadingZero(string[] versionSplit) {
        var vArr = new string[versionSplit.Length];
        for (int i = 0; i < versionSplit.Length; i++) {
            int p = 0;
            while (p < versionSplit[i].Length && versionSplit[i][p] == '0') p++;
            if (p == versionSplit[i].Length) vArr[i] = "0";
            else vArr[i] = versionSplit[i].Substring(p);
        }
        return vArr;
    }

    public int CompareVersion(string version1, string version2) {
        string[] version1_split = version1.Split('.');
        string[] version2_split = version2.Split('.');
        string[] vArr1 = TrimLeadingZero(version1_split);
        string[] vArr2 = TrimLeadingZero(version2_split);
        while (vArr1.Length < vArr2.Length) {
            Array.Resize(ref vArr1, vArr1.Length + 1);
            vArr1[vArr1.Length - 1] = "0";
        }
        while (vArr2.Length < vArr1.Length) {
            Array.Resize(ref vArr2, vArr2.Length + 1);
            vArr2[vArr2.Length - 1] = "0";
        }
        for (int i = 0; i < vArr2.Length; i++) {
            if (vArr1[i].Length > vArr2[i].Length) return 1;
            else if (vArr1[i].Length < vArr2[i].Length) return -1;
            else if (vArr1[i].CompareTo(vArr2[i]) > 0) return 1;
            else if (vArr1[i].CompareTo(vArr2[i]) < 0) return -1;
        }
        return 0;
    }
}

// @lc code=end

