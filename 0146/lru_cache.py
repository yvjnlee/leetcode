class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # learned about OrderedDict from editorial
        self.keys = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        self.keys.move_to_end(key)
        return self.keys[key]

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys.move_to_end(key)

        self.keys[key] = value

        if len(self.keys) > self.capacity:
            self.keys.popitem(0)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
