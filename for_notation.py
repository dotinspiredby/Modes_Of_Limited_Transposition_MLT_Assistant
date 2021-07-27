from process import total_check
from music21 import converter, metadata, serial


def notate_instr2(integerslist, index, modeid):
    notes = serial.ToneRow(integerslist).noteNames()
    parameters = ['%s/4' % len(notes)]
    for g in range(len(notes)):
        if int(integerslist[g]) < int(index):
            if notes[g][-1] in "#-":
                parameters.append(str(notes[g]).lower()[0] + "'" + str(notes[g]).lower()[-1] + "4")
            else:
                parameters.append(str(notes[g]).lower() + "'4")
        else:
            parameters.append(str(notes[g]).lower() + '4')
    parameters[-1] += '_MLT%s' % modeid + 't%s ' % index

    return '\t'.join(parameters)


def exctract_to_str(list_int, mode_id):
    list2 = []
    for tup in list_int:
        index_info, row = tup
        indx = index_info[-2]
        list2.append(str(notate_instr2(row, indx, mode_id)))

    return ''.join(list2)


def xml_export(row_data):
    notatn = []
    for m in range(len(row_data)):
        if len(row_data[m]) > 0:
            notatn.append(str(exctract_to_str(row_data[m], (m + 1))))
    notation = "tinyNotation: " + ' '.join(notatn)


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



