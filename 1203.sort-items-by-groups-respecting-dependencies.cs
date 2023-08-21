/*
 * @lc app=leetcode id=1203 lang=csharp
 *
 * [1203] Sort Items by Groups Respecting Dependencies
 */

// @lc code=start
public class Solution {
    public int[] SortItems(int n, int m, int[] group, IList<IList<int>> beforeItems) {
        List<List<int>> Groups = new List<List<int>>();
        for (int i = 0; i < m; i++)
        {
            Groups.Add(new List<int>());
        }
        int[] indexToGroup = new int[n];
        Array.Fill(indexToGroup, -1);
        for (int i = 0; i < n; i++)
        {
            if (group[i] == -1)
            {
                Groups.Add(new List<int>(new int[1] { i }));
                indexToGroup[i] = Groups.Count - 1;
            }
            else
            {
                Groups[group[i]].Add(i);
                indexToGroup[i] = group[i];
            }
        }

        m = Groups.Count;
        List<int[]>[] intraGroup = new List<int[]>[m];
        intraGroup = intraGroup.Select(x => new List<int[]>()).ToArray();
        List<int[]> interGroup = new List<int[]>();
        for (int i = 0; i < beforeItems.Count; i++)
        {
            foreach (int beforeItem in beforeItems[i])
            {
                if (indexToGroup[i] == indexToGroup[beforeItem])
                {
                    intraGroup[indexToGroup[i]].Add(new int[2] { beforeItem, i});
                }
                else
                {
                    interGroup.Add(new int[2] { indexToGroup[beforeItem], indexToGroup[i] });
                }                
            }
        }

        List<int> bfs;
        for (int i = 0; i < m; i++)
        {
            if (intraGroup[i].Count > 0)
            {
                bfs = TopoSort(Groups[i], intraGroup[i]);
                if (bfs.Count == Groups[i].Count)
                {
                    Groups[i] = bfs;
                }
                else
                {
                    return new int[0];
                }
            }
        }

        List<int> groupId = new List<int>();
        for (int i = 0; i < m; i++)
        {
            groupId.Add(i);
        }

        bfs = TopoSort(groupId, interGroup);
        List<int> result = new List<int>();
        if (bfs.Count == m)
        {
            foreach (int i in bfs)
            {
                foreach (int j in Groups[i])
                {
                    result.Add(j);
                }
            }
        }
        return result.ToArray();
    }
    
    private List<int> TopoSort(List<int> allElements, List<int[]> order) 
    {
        Dictionary<int, List<int>> G = new Dictionary<int, List<int>>();
        Dictionary<int, int> degree = new Dictionary<int, int>();
        
        foreach (int[] kvp in order) 
        {
            int j = kvp[0], k = kvp[1];
            if (!G.ContainsKey(j))
            {
                G.Add(j, new List<int>());
            }
            if (!degree.ContainsKey(k))
            {
                degree.Add(k, 0);
            }
            G[j].Add(k);
            degree[k]++;
        }
        
        Queue<int> queue = new Queue<int>();
        List<int> bfs = new List<int>();
        foreach (int j in allElements) 
        {
            if (!degree.ContainsKey(j)) 
            {
                queue.Enqueue(j);
                bfs.Add(j);
            }
        }

        while (queue.TryDequeue(out int node))
        {
            if (G.ContainsKey(node)) 
            {
                foreach (int k in G[node]) 
                {
                    degree[k]--;
                    if (degree[k] == 0) 
                    {
                        queue.Enqueue(k);
                        bfs.Add(k);                  
                    }
                }
            }
        } 
        return bfs;
    }
}

// @lc code=end

