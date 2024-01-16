import random

class RandomizedSet:

    def __init__(self):
        self.set_list = []
        self.set_hashmap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val not in self.set_hashmap:
            self.set_list.append(val)
            self.length += 1  
            self.set_hashmap[val] = self.length-1 
            return True
        return False     

    def remove(self, val: int) -> bool:
        if val in self.set_hashmap:
            index = self.set_hashmap[val]
            element = self.set_list[self.length-1]
            self.set_list[self.set_hashmap[val]],self.set_list[self.length-1] = self.set_list[self.length-1],self.set_list[self.set_hashmap[val]]
            self.set_hashmap[element] = index
            self.set_list.pop()
            del self.set_hashmap[val]
            self.length -=1
            return True
        return False
        

    def getRandom(self) -> int:
        i = random.randrange(0,self.length)
        return self.set_list[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
