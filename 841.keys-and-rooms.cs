/*
 * @lc app=leetcode id=841 lang=csharp
 *
 * [841] Keys and Rooms
 */

// @lc code=start
public class Solution 
{
    public bool CanVisitAllRooms(IList<IList<int>> rooms) 
    {
        Queue<int> queue = new Queue<int>();
        HashSet<int> visited = new HashSet<int>();
        int n = rooms.Count;

        queue.Enqueue(0);
        visited.Add(0);
        while (queue.TryDequeue(out int node))
        {
            foreach (int nxt in rooms[node])
            {
                if (!visited.Contains(nxt))
                {
                    queue.Enqueue(nxt);
                    visited.Add(nxt);
                }
            }
        }
        return (visited.Count == n);
    }
}
// @lc code=end

