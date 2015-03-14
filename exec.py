shebang = "#! /usr/bin/env python\n"


def is_exec(fname):
    with open(fname, 'r') as f:
        first_line = f.readline()
        if first_line == shebang:
            return True
        return False

print is_exec("file.txt")


def make_exec(fname):
    if not is_exec(fname):
        with open(fname, 'r+') as f:
            original_text = f.read()
            f.seek(0)
            f.write(shebang + original_text)

make_exec("file.txt")
