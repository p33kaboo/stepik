# class MyIterator:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = 0
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             print(self.iterable[self.index - 1])
#         raise StopIteration
#

def f2(x):
    return x % 2 == 0

def f3(x):
    return x % 3 == 0

class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина функций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, lst, *funcs, judge=judge_any):
        self.lst = lst
        self.judge = judge
        self.funcs = funcs

    def __iter__(self):
        for element in self.lst:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(element):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield element


print(list(multifilter([1,2,3,4,5,6,7,8,9,10], f2, f3)))
