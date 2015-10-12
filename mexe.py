import argparse
import os
import stat

__version__ = "0.0.2"

shebangs = {
    '2': b"#!/usr/bin/env python2\n",
    '3': b"#!/usr/bin/env python3\n",
    'default': b"#!/usr/bin/env python\n"
}


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', metavar="FILE", nargs='+',
                        help='file to be made executable')
    parser.add_argument("-p", "--pyversion", metavar="VERSION",
                        help="python version (2 or 3)")
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
        f.write(shebangs[version] + original_text)


def make_exec(fname, version):
    if version is None:
        version = 'default'
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
