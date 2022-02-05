class MyHashMap:

    def __init__(self):
        

    def put(self, key: int, value: int) -> None:
        

    def get(self, key: int) -> int:
        

    def remove(self, key: int) -> None:
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



# source: https://leetcode.com/problems/design-hashmap/discuss/1732515/python
class MyHashMap:
    def __init__(self):
        self.hashmap = {}
    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1
    def remove(self, key: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]