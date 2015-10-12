import argparse
import os
import stat

__version__ = "0.0.2"

shebangs = {
    '2': "#!/usr/bin/env python2\n",
    '3': "#!/usr/bin/env python3\n"
}


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('files', nargs='+', help='files to be made executable')
    parser.add_argument("-p", "--pyversion", help="select python version")
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__, help='show version')

    args = parser.parse_args()
    return args


def contains_shebang(f, version):
    first_line = f.readline()
    if first_line == shebangs[version]:
        return True
    return False


def put_shebang(f, version):
    if not contains_shebang(f, version):
        f.seek(0)
        original_text = f.read()
        f.seek(0)
        f.write(shebangs[version].encode('UTF-8') + original_text)


def make_exec(fname, version=3):
    with open(fname, 'rb+') as f:
        put_shebang(f, version)
    os.chmod(fname, os.stat(fname).st_mode | stat.S_IXOTH | stat.S_IXGRP |
             stat.S_IXUSR)
    print("{} is now executable".format(fname))


def main():

    args = parse_arguments()

    for dir in args.files:
        if os.path.isfile(dir):
            if dir.endswith(".py"):
                make_exec(dir, args.pyversion)
            else:
                print("{} is not a python file".format(dir))
        else:
            for filename in os.listdir(dir):
                if filename.endswith(".py"):
                    make_exec(filename, args.pyversion)
                else:
                    print("{} is not a python file".format(dir))

if __name__ == '__main__':
    main()
