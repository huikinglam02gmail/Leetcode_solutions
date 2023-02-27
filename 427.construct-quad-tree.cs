/*
 * @lc app=leetcode id=427 lang=csharp
 *
 * [427] Construct Quad Tree
 */

// @lc code=start

// Definition for a QuadTree node.
// public class Node {
//     public bool val;
//     public bool isLeaf;
//     public Node topLeft;
//     public Node topRight;
//     public Node bottomLeft;
//     public Node bottomRight;

//     public Node() {
//         val = false;
//         isLeaf = false;
//         topLeft = null;
//         topRight = null;
//         bottomLeft = null;
//         bottomRight = null;
//     }
    
//     public Node(bool _val, bool _isLeaf) {
//         val = _val;
//         isLeaf = _isLeaf;
//         topLeft = null;
//         topRight = null;
//         bottomLeft = null;
//         bottomRight = null;
//     }
    
//     public Node(bool _val,bool _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
//         val = _val;
//         isLeaf = _isLeaf;
//         topLeft = _topLeft;
//         topRight = _topRight;
//         bottomLeft = _bottomLeft;
//         bottomRight = _bottomRight;
//     }
// }

public class Solution 
{
    int[][] Grid;

    public Node helper(int x, int y, int n)
    {
        if (n == 1)
        {
            return new Node(Grid[x][y] == 1, true, null, null, null, null);
        }
        else
        {
            List<Node> quad = new List<Node>();
            for (int i = 0; i < 4; i++)
            {
                if (i == 0)
                {
                    quad.Add(helper(x, y, n / 2));
                }
                else if (i == 1)
                {
                    quad.Add(helper(x, y + n / 2, n / 2));
                }
                else if (i == 2)
                {
                    quad.Add(helper(x + n / 2, y, n / 2));
                }
                else
                {
                    quad.Add(helper(x + n / 2, y + n / 2, n / 2));                    
                }
            }

            bool allLeaves = true;
            bool allMatch = true;
            foreach (Node node in quad)
            {
                allLeaves &= node.isLeaf;
                allMatch &= (node.val == (Grid[x][y] == 1));
            }
            if (allLeaves && allMatch)
            {
                return new Node(Grid[x][y] == 1, true, null, null, null, null);
            }
            else
            {
                return new Node(true, false, quad[0], quad[1], quad[2], quad[3]);
            }
        }
    }

    public Node Construct(int[][] grid) 
    {
        Grid = grid;
        return helper(0, 0, grid.Length); 
    }
}
// @lc code=end

