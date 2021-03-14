cmd_stack = []
scopes = {'global': {
    'parent': None, 'variables': []
}
}
_len = int(input())  # сколько строк принять

for _ in range(_len):  # добавляю команды и значения в стак
    cmd, name, value = input().split()
    cmd_stack.append([cmd, name, value])

def create(name, value):
    global scopes
    scopes.setdefault(name, {
        'variables': [],
        'parent': value
    })
    return scopes

def add(name, value):
    global scopes
    scopes[name]['variables'].append(value)
    return scopes

def get(name, value):
    global scopes
    try:
        if value in scopes[name]['variables']:
            print(name)
        else:
            _prnt= scopes[name]['parent']
            return get(_prnt, value)
    except KeyError:
        print('None')

# вызов функций в зависимости от введенной комманды
for i in range(len(cmd_stack)):

    if cmd_stack[i][0] == 'create':
        create(cmd_stack[i][1], cmd_stack[i][2])

    elif cmd_stack[i][0] == 'add':
        add(cmd_stack[i][1], cmd_stack[i][2])

    else:
        get(cmd_stack[i][1], cmd_stack[i][2])

