/*
 * @lc app=leetcode id=1603 lang=csharp
 *
 * [1603] Design Parking System
 */

// @lc code=start
public class ParkingSystem
{
    private int BIG;
    private int MEDIUM;
    private int SMALL;

    public ParkingSystem(int big, int medium, int small)
    {
        BIG = big;
        MEDIUM = medium;
        SMALL = small;
    }

    public bool AddCar(int carType)
    {
        if (carType == 1)
        {
            if (BIG > 0)
            {
                BIG--;
                return true;
            }
            else
            {
                return false;
            }
        }
        if (carType == 2)
        {
            if (MEDIUM > 0)
            {
                MEDIUM--;
                return true;
            }
            else
            {
                return false;
            }
        }
        if (carType == 3)
        {
            if (SMALL > 0)
            {
                SMALL--;
                return true;
            }
            else
            {
                return false;
            }
        }
        return false;
    }
}


/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */
// @lc code=end

