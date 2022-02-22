

class Lisp_list_el:

    def __init__(self, el):

        self.el_str = None
        self.el_int = None
        self.el_list = None

        if type(el) == str:
            self.el_str = el
        elif type(el) == int:
            self.el_int = el
        elif type(el) == Lisp_list:
            self.el_list = el

    def for_print(self):
        if self.el_str != None:
            return "'" + self.el_str + "'"
        if self.el_int != None:
            return str(self.el_int)
        if self.el_list != None:
            return str(self.el_list)
        else:
            return 'None'


class Lisp_list:
    def __init__(self):
        self.list_ = []

    def add(self, el_):
        if el_.isnumeric():
            el = int(el_)
        elif el_[0] == '[' and el_[-1] == ']':
            elements = el_[1:-1].split(', ')
            el = Lisp_list()
            [el.add(x) for x in elements]
        else:
            el = el_

        self.list_.append(Lisp_list_el(el))

    def __str__(self):
        s = ', '.join([x.for_print() for x in self.list_])

        return '[' + s + ']'


lisp = Lisp_list()

print("FUNCTIONS:\n"
      "Print current list\n"
      "Clear list\n"
      "/*New value*/")

while(True):
    s = input()

    match s:
        case "Print current list":
            print(str(lisp))
        case "Clear list":
            lisp.list_ = []
        case _:
            lisp.add(s)
