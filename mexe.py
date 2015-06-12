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

    for dir in sys.argv[1:]:
        if os.path.isfile(dir):
            if dir.endswith(".py"):
                make_exec(dir)
                print("{} is now executable".format(dir))
            else:
                print("{} is not a python file".format(dir))
        else:
            for filename in os.listdir(dir):
                if file.endswith(".py"):
                    make_exec(filename)
                    print("{} is now executable".format(filename))

if __name__ == '__main__':
    main()
