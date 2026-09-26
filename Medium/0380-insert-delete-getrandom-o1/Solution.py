class RandomizedSet:

    def __init__(self):
        self.values = []
        self.valuesIdx = {} # value: index

    def insert(self, val: int) -> bool:
        if val in self.valuesIdx:
            return False
        
        self.valuesIdx[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.valuesIdx:
            return False
        
        index = self.valuesIdx[val]
        self.valuesIdx[self.values[-1]] = index
        del self.valuesIdx[val]
        self.values[index] = self.values[-1]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.values) - 1)
        return self.values[index]