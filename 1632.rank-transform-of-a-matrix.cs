/*
 * @lc app=leetcode id=1632 lang=csharp
 *
 * [1632] Rank Transform of a Matrix
 */

// @lc code=start
public class UnionFindSet
{
    public int[] parents{get; set;}
    public int count{get; set;} 
    public UnionFindSet(int n = 0)
    {
        parents = Enumerable.Range(0, n).ToArray();
        count = n;
    }

    public int find(int u)
    {
        if (u != parents[u])
        {
            parents[u] = find(parents[u]);
        }
        return parents[u];
    }

    public void union(int u, int v)
    {
        int pu = find(u);
        int pv = find(v);
        if (pu != pv)
        {
            int pMax = Math.Max(pu, pv);
            int pMin = Math.Min(pu, pv);
            parents[pMax] = pMin;
            count--;
        }
    }
}
public class Solution 
{
    public int[][] MatrixRankTransform(int[][] matrix) 
    {
        int m = matrix.Length;
        int n = matrix[0].Length;
        SortedDictionary<int, List<int[]>> hashTable = new SortedDictionary<int, List<int[]>>();
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!hashTable.ContainsKey(matrix[i][j]))
                {
                    hashTable.Add(matrix[i][j], new List<int[]>());
                }
                hashTable[matrix[i][j]].Add(new int[2]{i, j});
            }
        }

        int[][] result = new int[m][];
        for (int i = 0; i < m; i++)
        {
            result[i] = new int[n];
            Array.Fill(result[i], 0);
        }
        int[] rank = new int[m + n];
        Array.Fill(rank, 0);
        foreach (int value in hashTable.Keys)
        {
            UnionFindSet UF = new UnionFindSet(m + n);
            HashSet<int> changed = new HashSet<int>();
            foreach (int[] item in hashTable[value])
            {
                UF.union(item[0], item[1] + m);
                changed.Add(item[0]);
                changed.Add(item[1] + m);
            }
            int[] rankMax = new int[m + n];
            Array.Copy(rank, rankMax, m + n);
            foreach (int i in changed)
            {
                int j = UF.find(i);
                rankMax[j] = Math.Max(rankMax[j], rank[i]);
            }
            foreach (int i in changed)
            {
                rank[i] = rankMax[UF.find(i)] + 1;
            }           
            foreach (int[] item in hashTable[value])
            {
                result[item[0]][item[1]] = rank[item[0]];
            }
        }
        return result;
    }
}
// @lc code=end

