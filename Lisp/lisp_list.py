

class Lisp_list_el:
    def __init__(self, el):
        if type(el) == str:
            self.el_str = el
        elif type(el) == int:
            self.el_int = el
        elif type(el) == Lisp_list:
            self.el_list = el

    def for_print(self):
        if self.el_str != None:
            return self.el_str
        if self.el_int != None:
            return str(self.el_str)
        if self.el_list != None:
            return str(self.el_str)
        else:
            return


class Lisp_list:
    def __init__(self):
        self.list_ = []

    def add(self, el_):
        if el_.isnumeric():
            el = int(el_)
        if el_[0] == '[' and el_[-1] == ']':
            el = el_[1:-1].split(', ')


        self.list_.append(Lisp_list_el(el))

    def __str__(self):
        s = ', '.join([x for x in self.list_])

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
            print(lisp)
        case "Clear list":
            lisp.list_ = []
        case _:
            lisp.add(s)
