/*
 * @lc app=leetcode id=735 lang=csharp
 *
 * [735] Asteroid Collision
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * Use a stack to maintain the preexisting asteroids.
     * One important point is that the negative ones appearing left of the positive ones will never collide, so they will be ignored.
     * I used a collision_ended marker to indicate if any collision between an old positive asteroid in the stack and a new negative asteroid has been accounted for.
     * Note that I only turn it True when the incoming asteroid is larger than or equal to the incoming asteroid.
     */
    public int[] AsteroidCollision(int[] asteroids)
    {
        Stack<int> stack = new Stack<int>();
        foreach (int asteroid in asteroids)
        {
            if (stack.Count == 0)
            {
                stack.Push(asteroid);
            }
            else
            {
                bool collisionEnded = false;
                while (stack.Count > 0 && stack.Peek() >= 0 && asteroid < 0 && !collisionEnded)
                {
                    int old = stack.Pop();
                    collisionEnded = old + asteroid >= 0;
                    if (old + asteroid > 0)
                    {
                        stack.Push(old);
                    }
                }
                if (!collisionEnded)
                {
                    stack.Push(asteroid);
                }
            }
        }
        return stack.Reverse().ToArray();
    }
}

// @lc code=end

