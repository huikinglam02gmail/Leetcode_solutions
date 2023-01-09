#
# @lc app=leetcode id=1600 lang=python3
#
# [1600] Throne Inheritance
#

# @lc code=start
class ThroneInheritance:
    # At most 10^5 calls will be made to birth and death.
    # At most 10 calls will be made to getInheritanceOrder.
    # Therefore it makes sense to maintain a tree and conduct DFS whenever getInheritanceOrder is called
    # Also, we note that it might pay off if we keep a status of who is dead or alive
    def __init__(self, kingName: str):
        self.hashTable = {}
        self.hashTable[kingName] = {}
        self.hashTable[kingName]["alive"] = True
        self.hashTable[kingName]["children"] = []
        self.root = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.hashTable[parentName]["children"].append(childName)
        self.hashTable[childName] = {}
        self.hashTable[childName]["alive"] = True
        self.hashTable[childName]["children"] = []

    def death(self, name: str) -> None:
        self.hashTable[name]["alive"] = False

    def getInheritanceOrder(self) -> List[str]:
        return self.dfs(self.root)

    def dfs(self, person):
        result = []
        if self.hashTable[person]["alive"]:
            result.append(person)
        for child in self.hashTable[person]["children"]:
            result += self.dfs(child)
        return result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
# @lc code=end

