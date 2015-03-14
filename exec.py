import sys
import os

shebang = "#! /usr/bin/env python\n"


def is_exec(fname):
    with open(fname, 'r') as f:
        first_line = f.readline()
        if first_line == shebang:
            return True
        return False


def make_exec(fname):
    if not is_exec(fname):
        with open(fname, 'r+') as f:
            original_text = f.read()
            f.seek(0)
            f.write(shebang + original_text)


def main():
    if len(sys.argv) == 1:
        print("This program requires at least one parameter")
        sys.exit(1)

    for file in sys.argv[1:]:
        if os.path.isfile(file):
            make_exec(file)
            os.chmod(file, 0744)

if __name__ == '__main__':
    main()
