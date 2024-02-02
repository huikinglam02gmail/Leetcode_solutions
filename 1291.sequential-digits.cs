/*
 * @lc app=leetcode id=1291 lang=csharp
 *
 * [1291] Sequential Digits
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> SequentialDigits(int low, int high) {
        Queue<int> queue = new Queue<int>();
        List<int> result = new List<int>();

        for (int i = 1; i <= 9; i++) {
            queue.Enqueue(i);
        }

        while (queue.Count > 0) {
            int num = queue.Dequeue();

            if (low <= num && num <= high) {
                result.Add(num);
            }

            if (num <= high && num % 10 < 9) {
                queue.Enqueue(num * 10 + (num % 10 + 1));
            }
        }

        return result.OrderBy(x => x).ToList();
    }
}

// @lc code=end

