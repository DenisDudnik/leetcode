# https://leetcode.com/problems/lru-cache/


from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.values:
            self.values.move_to_end(key)
            return self.values[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if not self.capacity:
                self.values.popitem(last=False)
                self.capacity += 1
            self.capacity -= 1
        else:
            self.values.move_to_end(key)
        self.values[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lRUCache.get(2) == -1  # (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert lRUCache.get(1) == -1  # (not found)
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4
