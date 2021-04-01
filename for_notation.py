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


if __name__ == "__main__":
    xml_export([*total_check()])

