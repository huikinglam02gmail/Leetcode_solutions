
public class MyQueue 
{
    Stack<int> stack1;
    Stack<int> stack2;

    public MyQueue() 
    {
        stack1 = new Stack<int>();
        stack2 = new Stack<int>();    
    }

    public void clearance()
    {
        if (stack2.Count == 0)
        {
            while (stack1.Count > 0)
            {
                stack2.Push(stack1.Pop());
            }
        }
    }
    
    public void Push(int x) 
    {
        stack1.Push(x);    
    }
    
    public int Pop() 
    {
        clearance();
        return stack2.Pop();    
    }
    
    public int Peek() 
    {
        clearance();
        return stack2.Peek();   
    }
    
    public bool Empty() 
    {
        return stack1.Count + stack2.Count == 0;    
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */
// @lc code=end

