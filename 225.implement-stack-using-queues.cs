/*
 * @lc app=leetcode id=225 lang=csharp
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start
public class MyStack {

    Queue<int> queue1;
    Queue<int> queue2;
    public MyStack() {
        queue1 = new Queue<int>();
        queue2 = new Queue<int>();
    }
    
    public void Push(int x) {
        queue2.Enqueue(x);
        while (queue1.TryDequeue(out int y))
        {
            queue2.Enqueue(y);
        }
        queue1 = queue2;
        queue2 = new Queue<int>();
    }
    
    public int Pop() {
        return queue1.Dequeue();
    }
    
    public int Top() {
        return queue1.Peek();
    }
    
    public bool Empty() {
        return queue1.Count() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */
// @lc code=end

