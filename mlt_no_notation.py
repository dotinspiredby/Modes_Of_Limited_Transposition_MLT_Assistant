import tkinter as tk
from tkinter import *

app = Tk()
app.title("MLT Assistant")
app.geometry('375x500')
app.resizable(0, 0)

request = set()


def submit_pc(pc):
    request.add(pc)
    return request


def discard_pc(pc):
    request.discard(pc)
    return request


def run():
    return request


class Key:
    def __init__(self, data):
        self.n = Button(app)
        self.n.bind('<Button-1>', self.change)
        self.n.bind('<Button-3>', self.change_back)
        self.x = data[1]
        self.n.place(x=self.x, y=2)
        self.dig = data[0]
        self.n['state'] = NORMAL

    def change(self, event):
        self.n['bg'] = "#D7D7D7"
        submit_pc(self.dig)

    def change_back(self, event):
        discard_pc(self.dig)


class WhiteKey(Key):
    def __init__(self, data):
        super().__init__(data)
        self.n['width'] = 6
        self.n['height'] = 15
        self.n['bg'] = 'white'

    def change_back(self, event):
        self.new_sess()
        super().change_back(self.dig)

    def new_sess(self):
        self.n['bg'] = "white"


class BlackKey(Key):
    def __init__(self, data):
        super().__init__(data)
        self.n['width'] = 4
        self.n['height'] = 8
        self.n['bg'] = 'black'

    def change_back(self, event):
        self.new_sess()
        super().change_back(self.dig)

    def new_sess(self):
        self.n['bg'] = "black"


c = WhiteKey([0, 2])
d = WhiteKey([2, 55])
e = WhiteKey([4, 108])
f = WhiteKey([5, 161])
g = WhiteKey([7, 214])
a = WhiteKey([9, 267])
h = WhiteKey([11, 320])

cis = BlackKey([1, 32])
dis = BlackKey([3, 85])
fis = BlackKey([6, 191])
gis = BlackKey([8, 244])
b = BlackKey([10, 297])

keyboard = [c, d, e, f, g, a, h, cis, dis, fis, gis, b]

lbl = Label(app, text='Welcome to "Modes Of Limited Transposition Assistant" \n'
                      'Submit the notes to check them for the mode compatibility', font=("Palatino Linotype", 10))
lbl.place(x=1, y=340)

verdict = Text(width=45, height=10)


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


library = [[[i + 0] for i in range(0, 12, 2)],
           [[i, i + 1] for i in range(0, 12, 3)],
           [[i, i + 2, i + 3] for i in range(0, 12, 4)],
           [[i, i + 1, i + 2, i + 5] for i in range(0, 12, 6)],
           [[i, i + 1, i + 5] for i in range(0, 12, 6)],
           [[i, i + 2, i + 4, i + 5] for i in range(0, 12, 6)],
           [[i, i + 1, i + 2, i + 3, i + 5] for i in range(0, 12, 6)]]


def total_check(r):
    request2 = r
    verdict.place(x=4, y=380)
    for i in range(len(library)):
        st = '\n' + 'Mode of Limited Transposition: %s' % (i + 1) + '\n'
        mode_ed = construct(library[i])
        database = id_reg(mode_ed)
        result = [*validate(database, request2)]
        for g in result:
            st += str(g[0]) + '\t' + str(g[1]) + '\n'
        verdict.insert(0.1, st)
        yield result


def finalize(verdict):
    return verdict


def clear(event):
    verdict.delete("1.0", "end")
    for key in keyboard:
        key.change_back(event)
    lbl['text'] = 'New session started'


def newtext(event):
    lbl['text'] = 'The selected notes were found in the following modes:'


def new_win_size(event):
    app.geometry('375x700')
    new_search.place()
    verdict.place(x=4, y=380)


class FuncBtn:
    def __init__(self, descr):
        self.b = Button(app)
        self.b['width'] = 15
        self.b['height'] = 1
        self.b['text'] = descr[0]
        self.b['font'] = "Palatino Linotype", 11
        self.y = descr[1]
        self.b['command'] = descr[2]

    def place(self):
        self.b.place(x=4, y=self.y)

    def change_state(self):
        self.b['state'] = DISABLED

    def state_back(self):
        self.b['state'] = NORMAL


class FuncBtnp1(FuncBtn):
    def __init__(self, descr):
        super().__init__(descr)
        self.b.bind('<Button-1>', newtext)
        self.b.bind('<ButtonRelease-1>', new_win_size)

    def place(self):
        super().place()


class FuncBtnp2(FuncBtn):
    def __init__(self, descr):
        super().__init__(descr)

    def place(self):
        self.b.place(x=200, y=self.y)


submit = FuncBtnp1(['Search the modes', 280, lambda: finalize([*total_check(request)])])
submit.place()

new_search = FuncBtnp2(['New Session', 280, lambda: clear('<Button-1>')])

info = Label(app, text='Numbers in parenthesis indicate notes from c to h: \n'
             'c-0 cis/des-1 d-2 dis/es-3 e-4 f-5 fis-6 \n'
                       'g-7 gis/as-8 a-9 b/ais-10 b-11',
              font=("Palatino Linotype", 10))

info.place(x=4, y=580)

app.mainloop()
