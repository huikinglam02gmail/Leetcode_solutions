/*
 * @lc app=leetcode id=1462 lang=csharp
 *
 * [1462] Course Schedule IV
 */

// @lc code=start
public class Solution 
{
    public IList<bool> CheckIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) 
    {
        bool[][] reachable = new bool[numCourses][];
        HashSet<int>[] graph = new HashSet<int>[numCourses];
        HashSet<int>[] children = new HashSet<int>[numCourses];
        Queue<int> queue = new Queue<int>();
        HashSet<int> visited = new HashSet<int>();

         for (int i = 0; i < numCourses; i++)
        {
            graph[i] = new HashSet<int>();
            children[i] = new HashSet<int>();
            reachable[i] = new bool[numCourses];
            Array.Fill(reachable[i], false);
        }       

        for (int i = 0; i < prerequisites.Length; i++)
        {
            graph[prerequisites[i][0]].Add(prerequisites[i][1]);
        }

        for (int i = 0; i < numCourses; i++)
        {
            queue.Clear();
            visited.Clear();
            queue.Enqueue(i);
            visited.Add(i);
            while (queue.Count > 0)
            {
                int node = queue.Dequeue();
                foreach (int nxt in graph[node])
                {
                    if (nxt > i && !visited.Contains(nxt))
                    {
                        queue.Enqueue(nxt);
                        visited.Add(nxt);
                    }
                    else if (!reachable[i][nxt])
                    {
                        foreach (int item in children[nxt])
                        {
                            reachable[i][item] = true;
                            children[i].Add(item);
                        }
                    }
                    reachable[i][nxt] = true;
                    children[i].Add(nxt);
                }
            }
        }
        List<bool> result = new List<bool>();
        foreach(int[] query in queries)
        {
            result.Add(reachable[query[0]][query[1]]);
        }
        return result;
    }
}
// @lc code=end

