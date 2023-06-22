/*
 * @lc app=leetcode id=1769 lang=csharp
 *
 * [1769] Minimum Number of Operations to Move All Balls to Each Box
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int[] MinOperations(string boxes) {
        Queue<int> dq = new Queue<int>();
        int leftS = 0, rightS = 0, n = boxes.Length, leftCount = 0;
        List<int> result = new List<int>();

        for (int i = 0; i < n; i++) {
            if (boxes[i] == '1') {
                dq.Enqueue(i);
                rightS += i;
            }
        }

        for (int j = 0; j < n; j++) {
            if (dq.Count > 0 && j == dq.Peek()) {
                leftS += dq.Dequeue();
                rightS -= j;
                leftCount++;
            }

            result.Add(leftCount * j - leftS + rightS - dq.Count * j);
        }

        return result.ToArray();
    }
}

// @lc code=end

