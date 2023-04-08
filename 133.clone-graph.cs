/*
 * @lc app=leetcode id=133 lang=csharp
 *
 * [133] Clone Graph
 */

// @lc code=start
/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/
using System.Collections.Generic;

public class Solution 
{
    public Node CloneGraph(Node node) 
    {
        if (node is null)
        {
            return node;
        }

        Queue<Node> queue = new Queue<Node>(new Node[1] {node});
        Dictionary<int, Node> clones = new Dictionary<int, Node>();
        clones.Add(node.val, new Node(node.val, new List<Node>()));

        while (queue.TryDequeue(out Node curr))
        {
            Node currClone = clones[curr.val];
            foreach (Node neig in curr.neighbors)
            {
                if (!clones.ContainsKey(neig.val))
                {
                    clones.Add(neig.val, new Node(neig.val, new List<Node>()));
                    queue.Enqueue(neig);
                }
                currClone.neighbors.Add(clones[neig.val]);
            }
        }
        return clones[node.val];
    }
}
// @lc code=end

