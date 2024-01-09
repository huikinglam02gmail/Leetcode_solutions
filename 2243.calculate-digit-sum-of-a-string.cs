/*
 * @lc app=leetcode id=2243 lang=csharp
 *
 * [2243] Calculate Digit Sum of a String
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    /**
    Just simulate with a queue
    */
    public string DigitSum(string s, int k) {
        Queue<int> dq = new Queue<int>();
        foreach (char c in s) {
            dq.Enqueue(int.Parse(c.ToString()));
        }

        while (dq.Count > k) {
            int count = 0;
            List<int> current = new List<int> {0};

            while (dq.Count > 0) {
                while (count < k && dq.Count > 0) {
                    count++;
                    current[^1] += dq.Dequeue();
                }

                if (dq.Count > 0) {
                    count = 0;
                    current.Add(0);
                }
            }

            foreach (int num in current) {
                string numString = num.ToString();
                foreach (char c in numString) {
                    dq.Enqueue(int.Parse(c.ToString()));
                }
            }
        }

        StringBuilder result = new StringBuilder();
        while (dq.Count > 0) {
            result.Append(dq.Dequeue());
        }

        return result.ToString();
    }
}

// @lc code=end

