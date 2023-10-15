/*
 * @lc app=leetcode id=1947 lang=csharp
 *
 * [1947] Maximum Compatibility Score Sum
 */

// @lc code=start

using System;
using System.Collections.Generic;

public class Solution {
    private int[][] students;
    private int[][] mentors;
    private int m;
    private int n;
    private Dictionary<Tuple<int, int>, int> memo1;
    private Dictionary<Tuple<int, int>, int> memo;
    public int MaxCompatibilitySum(int[][] students, int[][] mentors) {
        this.students = students;
        this.mentors = mentors;
        this.m = students.Length;
        this.n = students[0].Length;
        memo1 = new Dictionary<Tuple<int, int>, int>();
        memo = new Dictionary<Tuple<int, int>, int>();
        return Backtracking(0, 0);
    }

    private int CompatibilityScore(int i, int j) 
    {
        Tuple<int, int> t = new Tuple<int, int>(i, j);
        if (!memo1.ContainsKey(t))
        {
            int score = 0;
            for (int k = 0; k < n; k++) {
                score += 1 - (students[i][k] ^ mentors[j][k]);
            }
            memo1.Add(t, score);            
        }
        return memo1[t];
    }

    

    private int Backtracking(int studentMask, int mentorMask) 
    {
        Tuple<int, int> t = new Tuple<int, int>(studentMask, mentorMask);
        if (!memo.ContainsKey(t))
        {
            int result = 0;

            for (int i = 0; i < m; i++) {
                if ((studentMask & (1 << i)) == 0) {
                    for (int j = 0; j < m; j++) {
                        if ((mentorMask & (1 << j)) == 0) {
                            result = Math.Max(result, CompatibilityScore(i, j) + Backtracking(studentMask | (1 << i), mentorMask | (1 << j)));
                        }
                    }
                }
            }

            memo[t] = result;            
        }
        return memo[t];
    }
}

// @lc code=end

