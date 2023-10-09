/*
 * @lc app=leetcode id=1938 lang=csharp
 *
 * [1938] Maximum Genetic Difference Query
 */

// @lc code=start
using System.Linq;
public class Solution
{
    private List<int[]>[] queryDict;
    private int[] result;
    private HashSet<int>[] graph;
    private int totalLevels;
    private int[][] prefixTree;
    private void dfs(int node)
    {
        addNumToPrefixArray(node);
        foreach (int[] query in queryDict[node])
        {
            result[query[0]] = getMaximumXOR(query[1]);
        }
        foreach (int child in graph[node])
        {
            dfs(child);
        }
        removeNumToPrefixArray(node);
    }

    private void addNumToPrefixArray(int num)
    {
        for (int i = totalLevels - 1; i >= 0; --i)
        {
            prefixTree[i][num >> i]++;
        }
    }

    private void removeNumToPrefixArray(int num)
    {
        for (int i = totalLevels - 1; i >= 0; --i)
        {
            prefixTree[i][num >> i]--;
        }
    }

    private int getMaximumXOR(int val)
    {
        int result = 0;
        for (int i = totalLevels - 1; i >= 0; --i)
        {
            int valBit = (val >> i) & 1;
            result <<= 1;
            result += (prefixTree[i][result + 1 - valBit]) > 0 ? 1 - valBit : valBit;
        }
        return result ^ val;
    }
    
    public static int bitLength(int bits)
    {
        var size = 0;
        while(bits != 0)
        {
            bits >>= 1;
            size++;
        }
        return size;
    }

    public int[] MaxGeneticDifference(int[] parents, int[][] queries) 
    {
        int n = parents.Length;
        graph = new HashSet<int>[n];
        graph = graph.Select(x => new HashSet<int>()).ToArray();
        queryDict = new List<int[]>[n];
        queryDict = queryDict.Select(x => new List<int[]>()).ToArray();
        result = new int[queries.Length];
        result = result.Select(x => -1).ToArray();
        totalLevels = bitLength(Math.Max(n - 1, queries.Select(x => x[1]).Max()));
        prefixTree = new int[totalLevels][];
        for (int i = 0; i < totalLevels; ++i)
        {
            prefixTree[i] = new int[1 << (totalLevels - i)];
            Array.Fill(prefixTree[i], 0);
        }

        int root = -1;
        for (int i = 0; i < n; ++i)
        {
            if (parents[i] != -1)
            {
                graph[parents[i]].Add(i);
            }
            else
            {
                root = i;
            }
        }

        for (int i = 0; i < queries.Length; i++)
        {
            queryDict[queries[i][0]].Add(new int[2]{i, queries[i][1]});
        }

        dfs(root);
        return result;
    }
}
// @lc code=end

