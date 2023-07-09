/*
 * @lc app=leetcode id=2272 lang=csharp
 *
 * [2272] Substring With Largest Variance
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string.
    So we need to consider any two pairs. Because we only need to consider 26 * 26 = 676 character pairs, and within each pair, all other characters are irrelevant. for pair ("a", "b"), we are assign "a" = +1 and "b" = -1, and all characters will not enter the List. This problem is then a maximum subarray sum problem, solvable by Kadane. There is a catch though: unlike in Kadane, we would like ensure all the subarrays of interest has both "a" and "b"
    */

    public int Kadane(List<int> arr) {
        int current = 0;
        int result = 0;
        bool beginMinus = false;
        bool hasMinus = false;
        
        foreach (int num in arr) {
            if (num == -1) {
                hasMinus = true;
                if (current >= 0 && beginMinus) {
                    beginMinus = false;
                    current += 1;
                }
            }
            
            current += num;
            
            if (current < 0) {
                current = -1;
                beginMinus = true;
            }
            else if (hasMinus) {
                result = Math.Max(result, current);
            }
        }
        
        return result;
    }

    public int LargestVariance(string s) {
        int result = 0;
        List<List<int>> occur = new List<List<int>>(26);

        for (int i = 0; i < 26; i++) {
            occur.Add(new List<int>());
        }

        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            occur[c - 'a'].Add(i);
        }

        for (int i = 0; i < 25; i++) {
            for (int j = i + 1; j < 26; j++) {
                if (occur[i].Count > 0 && occur[j].Count > 0) {
                    List<int> subArray = new List<int>();
                    int pi = 0;
                    int pj = 0;

                    // Two pointers merge
                    while (pi < occur[i].Count && pj < occur[j].Count) {
                        if (occur[i][pi] < occur[j][pj]) {
                            subArray.Add(1);
                            pi += 1;
                        }
                        else {
                            subArray.Add(-1);
                            pj += 1;
                        }
                    }
                    
                    while (pi < occur[i].Count) {
                        subArray.Add(1);
                        pi += 1;
                    }
                    
                    while (pj < occur[j].Count) {
                        subArray.Add(-1);
                        pj += 1;
                    }
                    
                    result = Math.Max(result, Kadane(subArray));
                    result = Math.Max(result, Kadane(subArray.ConvertAll(x => -x)));
                }
            }
        }
        
        return result;
    }
}

// @lc code=end

