def is_exec(fname):
    shebang = "#! /usr/bin/env python\n"
    with open(fname, 'r') as f:
        first_line = f.readline()
        if first_line == shebang:
            return True
        return False

print is_exec("file.txt")
