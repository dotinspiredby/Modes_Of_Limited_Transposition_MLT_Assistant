from mode_constructor import library


def construct(gen):
    c_mode = set()
    for i in range(len(gen)):
        for j in range(len(gen[0])):
            c_mode.add(gen[i][j])
    return c_mode


def transpose(s, i=0):
    transposed = set()
    for elem in s:
        k = int((elem + i) % 12)
        transposed.add(k)
    return transposed


def id_reg(mode):
    reg = [mode]
    for i in range(1, 6):
        t = transpose(mode, i)
        if t != mode:
            reg.append(t)
        else:
            break
    return reg


def validate(lib, data_set):
    for i in range(len(lib)):
        if data_set <= lib[i]:
            resulted = list(lib[i])
            while resulted[0] != i:
                resulted.insert(len(resulted), resulted[0])
                resulted.remove(resulted[0])
            yield 'transposition index %s:' % i, resulted


def total_check():
    print('Type your tone request using integers from 0 to 11 (c-b/h):')
    try:
        request = set(map(int, input().split()))
        for i in range(len(library)):
            mode_ed = construct(library[i])
            database = id_reg(mode_ed)
            result = [*validate(database, request)]
            print('\n' + 'MLT: %s' % (i + 1), *result, sep='\n')
            yield result
    except ValueError:
        print('Please, try again - use only integers from 0 to 11')
        total_check()


if __name__ == "__main__":
    total_check()


