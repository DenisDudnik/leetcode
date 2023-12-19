# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:

    # def __init__(self):
    #     self.data = set()
    #     self.count = 0

    # def insert(self, val: int) -> bool:
    #     self.data.add(val)
    #     if (count := len(self.data)) != self.count:
    #         self.count = count
    #         return True
    #     return False

    # def remove(self, val: int) -> bool:
    #     self.data.discard(val)
    #     if (count := len(self.data)) != self.count:
    #         self.count = count
    #         return True
    #     return False

    # def getRandom(self) -> int:
    #     if self.count:
    #         return random.choice(list(self.data))
    #     return None

    def __init__(self):
        self.data = dict()

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        
        self.data[val] = True
        return True

    def remove(self, val: int) -> bool:
        res = self.data.pop(val, False)
        return res

    def getRandom(self) -> int:
        if len(self.data):
            return random.choice(list(self.data.keys()))
        return None


if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.data)
    assert randomizedSet.insert(1) == True
    print(randomizedSet.data)
    assert randomizedSet.remove(2) == False
    print(randomizedSet.data)
    assert randomizedSet.insert(2) == True
    print(randomizedSet.data)
    assert randomizedSet.getRandom() in [1,2]
    assert randomizedSet.remove(1) == True
    print(randomizedSet.data)
    assert randomizedSet.insert(2) == False
    print(randomizedSet.data)
    assert randomizedSet.getRandom() == 2
