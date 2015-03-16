#! /usr/bin/env python
import sys
import os

shebang = "#! /usr/bin/env python\n"


def contains_shebang(fname):
    with open(fname, 'r') as f:
        first_line = f.readline()
        if first_line == shebang:
            return True
        return False


def put_shebang(fname):
    if not contains_shebang(fname):
        with open(fname, 'r+') as f:
            original_text = f.read()
            f.seek(0)
            f.write(shebang + original_text)


def make_exec(fname):
    put_shebang(fname)
    os.chmod(fname, 0755)


def main():
    if len(sys.argv) == 1:
        print("This program requires at least one parameter.")
        sys.exit(1)

    for file in sys.argv[1:]:
        if os.path.isfile(file):
            make_exec(file)
            print("{0} is now executable".format(file))

if __name__ == '__main__':
    main()
