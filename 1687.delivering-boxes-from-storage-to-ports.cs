/*
 * @lc app=leetcode id=1687 lang=csharp
 *
 * [1687] Delivering Boxes from Storage to Ports
 */

// @lc code=start

using System.Collections.Generic;

/**
Break down the question into basics. If there are no limits on maxBoxes and maxWeight, the number of trips is 1 (start from storage) + number of transitions in boxes[:][0] + 1 (go back to storage).
When we put in the constraints, we increase the minimum cost. We can break this problem into subproblems:
Let dp(i) = minimum number of additional trips above base line the ship needs to make to deliver boxes[:i+1] to their respective ports. (returning back to the storage port at the end). We want to get dp(n-1). 
if we finished box[:i] and we want to deliver box[i], we can attempt the following: choose a port j (j + 1 <= i) in which we transport boxes[j + 1:i + 1] in one single trip. The additional cost we will add to the base cost is:
1. if boxes[i][0] == boxs[i + 1][0], we add 2 (base case does not go back to storage port, we add 2 trips)
2. else, just add 1 (as boxes[i][0] != boxes[i+1][0], instead of going directly from boxes[i][0] to boxes[i+1][0] we add 1 trip to go back to storage port)
We have the recursive relation: dp(i) = min(dp[j:i]) + 1(if boxes[i][0] != boxes[i+1][0]) else + 2 
There is no need to scan all the j-i pairs because if we know box[j:i+ 1] does not satisfy the constraint, box[j-1: i + 1] won't either. Instead we use the monotonic increasing queue and to make sure the smallet dp value is always on the left end
**/
public class Solution 
{
    public int BoxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) 
    {
        int n = boxes.Length;
        LinkedList<int[]> queue = new LinkedList<int[]>();
        queue.AddLast(new int[2]{-1, 1});

        int left = -1;
        int weight = 0;
        int currentCost = 0;
        for (int i = 0; i < n; i++)
        {
            weight += boxes[i][1];
            while ((i - left) > maxBoxes || weight > maxWeight)
            {
                left++;
                weight -= boxes[left][1];
            }
            while (queue.Count > 0 && queue.First.Value[0] < left)
            {
                queue.RemoveFirst();
            }

            currentCost = queue.First.Value[1] + 1;
            if (i < n - 1 && boxes[i][0] == boxes[i + 1][0])
            {
                currentCost++;
            }
            while (queue.Count > 0 && queue?.Last.Value[1] >= currentCost)
            {
                queue.RemoveLast();
            }
            queue.AddLast(new int[2]{i, currentCost});
        }

        for (int i = 0; i < n - 1; i++)
        {
            if (boxes[i][0] != boxes[i + 1][0])
            {
                currentCost++;
            }
        }
        return currentCost;
    }
}
// @lc code=end

