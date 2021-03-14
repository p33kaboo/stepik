class ExtendedStack(list):
    def sum(self):
        if len(self) >= 2:
            self.append(self[-2] + self.pop())
            del self[-2]
        print(self)

    def sub(self):
        if len(self) >= 2:
            self.append(self.pop() - self[-1])
            del self[-2]
        print(self)

    def mul(self):
        if len(self) >= 2:
            self.append(self[-2] * self.pop())
            del self[-2]
        print(self)

    def div(self):
        if len(self) >= 2:
            self.append(self.pop() // self[-1])
            del self[-2]

        print(self)


my_func = ExtendedStack([1, 2,3])

my_func.sum()
my_func.sub()
my_func.mul()
my_func.div()
