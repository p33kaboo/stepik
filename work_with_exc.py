class OmgError(Exception):
    pass


def greeting(name):
    if name[0].isupper():
        print(f"Hello, {name}")
    else:
        raise OmgError(f'Smth wrong with your inputed text!')


while True:
    try:

        # name = input('Enter your name: ')
        #greeting(name)
        pass
    except:
        print('Try again! ')
    else:
        break


class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError('Error')


pos = PositiveList()

pos.append(int(input()))

print(pos)






















