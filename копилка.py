class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
    def can_add(self, v):
        return self.count + v <= self.capacity
    def add(self, v):
        if self.can_add(v):
            self.count += v


mb = MoneyBox(10)

mb.can_add(9)
mb.add(5)
print(mb.count)