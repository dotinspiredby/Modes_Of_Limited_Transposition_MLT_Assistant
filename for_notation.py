from process import total_check
from music21 import converter, metadata, serial


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


def exctract_to_str(list_int, index, mode_id):
    indx = index
    list2 = []
    end_of_unpacking = False
    for i in list_int:
        if isinstance(i, int):
            end_of_unpacking = True
        elif isinstance(i, tuple):
            index_info, row = i
            indx = index_info[-2]
            list2 = row
    if end_of_unpacking:
        return notate_instr2(list_int, indx, mode_id)
    else:
        return exctract_to_str(list2, indx, mode_id)


def xml_export(row_data):
    notation = 'tinyNotation: '
    for m in range(len(row_data)):
        if len(row_data[m]) > 0:
            notation += str(*exctract_to_str(row_data[m], None, m + 1))

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


if __name__ == "__main__":
    xml_export([*total_check()])

