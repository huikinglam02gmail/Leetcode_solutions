/*
 * @lc app=leetcode id=1494 lang=csharp
 *
 * [1494] Parallel Courses II
 */

// @lc code=start
public class Solution 
{
    List<List<int>> combinationIndicies;
    List<int> tmp;

    public void makeCombiUtil(int n, int left, int k)
    {
        // Pushing this vector to a vector of vector
        if (k == 0) 
        {
            combinationIndicies.Add(tmp.Select(s => s).ToList());
            return;
        }
  
        // i iterates from left to n - 1. First time left will be 0
        for (int i = left; i < n; i++)
        {
            tmp.Add(i);
            makeCombiUtil(n, i + 1, k - 1);
  
            // Popping out last inserted element from the vector
            tmp.RemoveAt(tmp.Count - 1);
        }
    }

    public int MinNumberOfSemesters(int n, int[][] relations, int k) 
    {
        int[] dp = new int[1 << n];
        int[] pre = new int[n];
        Queue<int[]> queue = new Queue<int[]>();

        Array.Fill(dp, n + 1);
        dp[0] = 0;
        Array.Fill(pre, 0);
        foreach (int[] relation in relations)
        {
            pre[relation[1]-1] += 1 << (relation[0]-1);
        }

        queue.Enqueue(new int[2]{0,0});
        while (queue.Count > 0)
        {
            int[] item = queue.Dequeue();
            int mask = item[0];
            int semester = item[1];
            if (mask == ((1 << n) - 1))
            {
                return semester;
            }
            List<int> candidate = new List<int>();
            for (int i = 0; i < n; i++)
            {
                if (((mask & (1 << i)) == 0) && ((mask & pre[i]) == pre[i]))
                {
                    candidate.Add(i);
                }
            }
            List<List<int>> candidates = new List<List<int>>();
            if (candidate.Count <= k)
            {
                candidates.Add(candidate);
            }
            else
            {
                combinationIndicies = new List<List<int>>();
                tmp = new List<int>();
                makeCombiUtil(candidate.Count, 0, k);
                foreach (List<int> indices in combinationIndicies)
                {
                    List<int> candidatePick = new List<int>();
                    foreach (int index in indices)
                    {
                        candidatePick.Add(candidate[index]);
                    }
                    candidates.Add(candidatePick);
                }
            }
            foreach (List<int> cand in candidates)
            {
                int newMask = mask;
                foreach (int j in cand)
                {
                    newMask += (1 << j);
                }
                if (dp[newMask] > semester + 1)
                {
                    dp[newMask] = semester + 1;
                    queue.Enqueue(new int[] {newMask, semester + 1});
                }
            }
        }
        return n;
    }
}
// @lc code=end

