class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            # Remove the value from the list here
            index = self.dict[val]
            self.list[index] = self.list[-1]
            self.dict[self.list[-1]] = index
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)
