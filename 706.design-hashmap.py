class MyHashMap:

    def __init__(self):
        self._hashmap = dict()

    def put(self, key: int, value: int) -> None:
        self._hashmap[key] = value

    def get(self, key: int) -> int:
        if key not in self._hashmap:
            return -1
        return self._hashmap[key]

    def remove(self, key: int) -> None:
        if key in self._hashmap.keys():
            del self._hashmap[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)