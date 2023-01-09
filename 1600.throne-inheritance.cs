/*
 * @lc app=leetcode id=1600 lang=csharp
 *
 * [1600] Throne Inheritance
 */

// @lc code=start
public class ThroneInheritance {

    Dictionary<string, bool> alive;
    Dictionary<string, List<string>> children;
    string root;
    public ThroneInheritance(string kingName) 
    {
        alive = new Dictionary<string, bool>();
        alive.Add(kingName, true);
        children = new Dictionary<string, List<string>>();
        children.Add(kingName, new List<string>());
        root = kingName;
    }
    
    public void Birth(string parentName, string childName) 
    {
        children[parentName].Add(childName);
        alive.Add(childName, true);
        children.Add(childName, new List<string>());
    }
    
    public void Death(string name) 
    {
        alive[name] = false;    
    }
    
    public IList<string> GetInheritanceOrder() 
    {
        return dfs(root);    
    }

    public List<string> dfs(string person)
    {
        List<string> result = new List<string>();
        if (alive[person])
        {
            result.Add(person);
        }
        foreach (string child in children[person])
        {
            result.AddRange(dfs(child));
        }
        return result;
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = new ThroneInheritance(kingName);
 * obj.Birth(parentName,childName);
 * obj.Death(name);
 * IList<string> param_3 = obj.GetInheritanceOrder();
 */
// @lc code=end
