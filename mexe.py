import sys
import os
import stat

shebang = "#!/usr/bin/env python\n"


def contains_shebang(f):
        first_line = f.readline()
        if first_line == shebang:
            return True
        return False


def put_shebang(f):
    if not contains_shebang(f):
        f.seek(0)
        original_text = f.read()
        f.seek(0)
        f.write(shebang + original_text)


def make_exec(fname):
    with open(fname, 'rb+') as f:
        put_shebang(f)
    os.chmod(fname, os.stat(fname).st_mode | stat.S_IXOTH | stat.S_IXGRP |
             stat.S_IXUSR)


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
                if filename.endswith(".py"):
                    make_exec(filename)
                    print("{} is now executable".format(filename))

if __name__ == '__main__':
    main()
