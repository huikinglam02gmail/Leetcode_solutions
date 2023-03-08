/*
 * @lc app=leetcode id=1670 lang=csharp
 *
 * [1670] Design Front Middle Back Queue
 */

// @lc code=start
using System.Collections.Generic;
public class FrontMiddleBackQueue 
{

    LinkedList<int> left;
    LinkedList<int> right; 


    public FrontMiddleBackQueue() 
    {
        left = new LinkedList<int>();
        right = new LinkedList<int>();    
    }

    public void balance()
    {
        while (left.Count > right.Count)
        {   
            int value = left.Last.Value;
            right.AddFirst(value);
            left.RemoveLast();
        }        
        while (right.Count > left.Count + 1)
        {
            int value = right.First.Value;
            left.AddLast(value);
            right.RemoveFirst();
        }
    }
    
    public void PushFront(int val) 
    {
        left.AddFirst(val);
        balance();
    }
    
    public void PushMiddle(int val) 
    {
        left.AddLast(val);
        balance();
    }
    
    public void PushBack(int val) 
    {
        right.AddLast(val);
        balance();
    }
    
    public int PopFront() 
    {
        int result = -1;
        if (left.Count > 0)
        {
            result = left.First.Value;
            left.RemoveFirst();
        }
        else if (right.Count > 0)
        {
            result = right.First.Value;
            right.RemoveFirst();
        }
        balance();  
        return result;        
    }
    
    public int PopMiddle() 
    {
        int result = -1;
        if (right.Count > 0)
        {
            if (left.Count == right.Count)
            {
                result = left.Last.Value;
                left.RemoveLast();
            }
            else if (left.Count < right.Count)
            {
                result = right.First.Value;
                right.RemoveFirst();
            }
            balance();
        }    
        return result;
    }
    
    public int PopBack() 
    {
        int result = -1;
        if (right.Count > 0)
        {
            result = right.Last.Value;
            right.RemoveLast();
            balance();
        }    
        return result;
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.PushFront(val);
 * obj.PushMiddle(val);
 * obj.PushBack(val);
 * int param_4 = obj.PopFront();
 * int param_5 = obj.PopMiddle();
 * int param_6 = obj.PopBack();
 */
// @lc code=end

