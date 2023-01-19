/*
 * @lc app=leetcode id=1625 lang=csharp
 *
 * [1625] Lexicographically Smallest String After Applying Operations
 */

// @lc code=start
public class Solution 
{
    public string FindLexSmallestString(string s, int a, int b) 
    {
        Queue<string> queue = new Queue<string>();
        HashSet<string> visited = new HashSet<string>();    
        string result = s;

        queue.Enqueue(s);
        visited.Add(s);
        while (queue.TryDequeue(out string node))
        {
            if (string.Compare(node, result) < 0)
            {
                result = node;
            }
            StringBuilder newNode1 = new StringBuilder();
            StringBuilder newNode2 = new StringBuilder();
            for (int i = 0; i < node.Length; i++)
            {
                if ( i % 2 == 1)
                {
                    newNode1.Append(((Int32.Parse(node[i].ToString()) + a) % 10).ToString());
                }
                else
                {
                    newNode1.Append(node[i]);
                }
                newNode2.Append(node[( i + b ) % s.Length]);
            }
            string newNodeString1 = newNode1.ToString();
            string newNodeString2 = newNode2.ToString();
            if (!visited.Contains(newNodeString1))
            {
                queue.Enqueue(newNodeString1);
                visited.Add(newNodeString1);
            }
            if (!visited.Contains(newNodeString2))
            {
                queue.Enqueue(newNodeString2);
                visited.Add(newNodeString2);
            }
        }
        return result;

    }
}
// @lc code=end

