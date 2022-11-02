/*
 * @lc app=leetcode id=433 lang=csharp
 *
 * [433] Minimum Genetic Mutation
 */

// @lc code=start
public class Solution {
    public bool canMutate(string start, string end)
    {
        int count = 0;
        for (int i = 0; i < 8; i++)
        {
            if (start[i] != end[i])
            {
                count += 1;
            }
        }
        return count <= 1;
    }
    public int MinMutation(string start, string end, string[] bank) {
        int count = 0;
        foreach (string seq in bank)
        {
            if (canMutate(start, seq))
            {
                count += 1;
            }
        }
        if (count == 0)
        {
            return -1;
        }
        HashSet<string> bankSet = bank.ToHashSet();
        if (!bankSet.Contains(end))
        {
            return -1;
        }

        Queue<string> queue = new Queue<string>();
        int steps = 0;
        queue.Enqueue(start);
        while (queue.Count > 0)
        {
            int n = queue.Count;
            HashSet<string> toRemove = new HashSet<string>();
            for (int i = 0; i < n; i++)
            {
                string last = queue.Dequeue();
                if (last == end)
                {
                    return steps;
                }
                foreach (string nxt in bankSet)
                {
                    if (canMutate(last, nxt))
                    {
                        toRemove.Add(nxt);
                    }
                }
            }
            foreach (string item in toRemove)
            {
                queue.Enqueue(item);
                bankSet.Remove(item);
            }
            steps += 1;
        }
        return -1;
    }
}
// @lc code=end

