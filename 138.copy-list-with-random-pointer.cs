/*
 * @lc app=leetcode id=138 lang=csharp
 *
 * [138] Copy List with Random Pointer
 */

// @lc code=start
/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node CopyRandomList(Node head) {
        if (head == null) return null;

        Node temp = head;
        int i = 0;
        List<Node> newList = new List<Node>();
        Dictionary<int, int> indexMap = new Dictionary<int, int>();

        while (temp != null) {
            Node newNode = new Node(temp.val);
            if (newList.Count > 0) {
                newList[newList.Count - 1].next = newNode;
            }
            newList.Add(newNode);

            temp.val = i * 20001 + (temp.val + 10000);
            indexMap[temp.val] = i;
            temp = temp.next;
            i++;
        }

        temp = head;

        while (temp != null) {
            if (temp.random != null) {
                newList[indexMap[temp.val]].random = newList[indexMap[temp.random.val]];
            }
            temp = temp.next;
        }

        return newList.Count == 0 ? null : newList[0];
    }
}
// @lc code=end

