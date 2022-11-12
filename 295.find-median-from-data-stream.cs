/*
 * @lc app=leetcode id=295 lang=csharp
 *
 * [295] Find Median from Data Stream
 */

// @lc code=start
public class MedianFinder {
    PriorityQueue<int, int> small;
    PriorityQueue<int, int> large;
    public MedianFinder() {
        small = new PriorityQueue<int, int>();
        large = new PriorityQueue<int, int>();
    }
    
    public void AddNum(int num) 
    {
        if (small.Count > 0 && num >= small.Peek())
        {
            large.Enqueue(num, num);
        }
        else
        {
            small.Enqueue(num, -num);
        }
        while (Math.Abs(small.Count - large.Count) > 1)
        {
            if (small.Count > large.Count)
            {
                int item = small.Dequeue();
                large.Enqueue(item, item);
            }
            else
            {
                int item = large.Dequeue();
                small.Enqueue(item, -item);
            }
        }
    }
    
    public double FindMedian() 
    {
        if ((small.Count + large.Count)%2 == 0)
        {
            return ((double) small.Peek() + (double) large.Peek()) / 2;
        }
        else if (small.Count > large.Count)
        {
            return (double) small.Peek();
        }
        else
        {
            return (double) large.Peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.AddNum(num);
 * double param_2 = obj.FindMedian();
 */
// @lc code=end

