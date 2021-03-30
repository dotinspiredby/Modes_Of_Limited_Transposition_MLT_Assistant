from music21 import converter, metadata, serial


def construct(gen):
    c_mode = set()
    for i in range(len(gen)):
        for j in range(len(gen[0])):
            c_mode.add(gen[i][j])
    return c_mode


def transpose(s, i=0):
    transposed = set()
    for elem in s:
        k = int((elem+i) % 12)
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


library = [[[i+0] for i in range(0, 12, 2)],
           [[i, i+1] for i in range(0, 12, 3)],
           [[i, i+2, i+3] for i in range(0, 12, 4)],
           [[i, i+1, i+2, i+5] for i in range(0, 12, 6)],
           [[i, i+1, i+5] for i in range(0, 12, 6)],
           [[i, i+2, i+4, i+5] for i in range(0, 12, 6)],
           [[i, i+1, i+2, i+3, i+5] for i in range(0, 12, 6)]]


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


def notate_instr2(integerslist, index, modeid):
    notes = serial.ToneRow(integerslist).noteNames()
    parameters = '%s/4' % len(notes)
    for g in range(len(notes)):
        if int(integerslist[g]) < int(index):
            if notes[g][-1] in "#-":
                notes[g] = str(notes[g]).lower()[0] + "'" + str(notes[g]).lower()[-1] + "4"
            else:
                notes[g] = str(notes[g]).lower() + "'4"
        else:
            notes[g] = str(notes[g]).lower() + '4'
    notes[-1] += '_MLT%s' % modeid + 't%s ' % index
    for g in notes:
        parameters += '\t' + g
    yield parameters


def xml_gather2(lofl, modeid):
    for i in range(len(lofl)):
        instr = ''.join(notate_instr2(lofl[i][1], index=lofl[i][0][-2], modeid=modeid))
        yield instr


def pre_xmlexport(mode, modeid):
    i = ''.join(xml_gather2(lofl=mode, modeid=modeid))
    yield i


def xml_export(row_data):
    notation = 'tinyNotation: '
    for m in range(len(row_data)):
        if len(row_data[m]) > 0:
            notation += ''.join(*pre_xmlexport(row_data[m], (m + 1)))

    if input('\n''Would you like your printed XML copy (yes/no)?') == 'yes':
        s = converter.parse(notation)
        s.insert(0, metadata.Metadata())
        s.metadata.title = input('Enter the title of the piece for your analysis:')
        s.metadata.composer = 'MLT Assistant for %s' % input('Enter the composer:')
        s.show()
    if input('Start new search (yes/no)?') == 'yes':
        print('New session started.')
        xml_export([*total_check()])
    else:
        print('Good luck with "Modes of Limited Transposition!"')


xml_export([*total_check()])
