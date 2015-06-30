import unittest
import os
import stat
import sys
sys.path.insert(0, os.path.abspath('..'))

import mexe


class TestHelperFunctions(unittest.TestCase):

    def test_contains_shebang(self):
        with open("hello.py", 'w+') as f:
            mexe.put_shebang(f)
        with open("hello.py", 'r') as f:
            self.assertTrue(mexe.contains_shebang(f))
        os.remove("hello.py")

    def test_not_contains_shebang(self):
        with open("hello.py", 'w+') as f:
            f.seek(0)
            f.write("some random text")
        with open("hello.py", 'r') as f:
            self.assertFalse(mexe.contains_shebang(f))
        os.remove("hello.py")

    def test_put_shebang(self):
        shebang = "#!/usr/bin/env python\n"
        with open("hello.py", "w+") as f:
            mexe.put_shebang(f)
        with open("hello.py", 'r') as f:
            self.assertEqual(f.readline(), shebang)
        os.remove("hello.py")

    def test_make_exec(self):
        mexe.make_exec("hello.py")
        st = os.stat("hello.py")
        self.assertTrue(bool(st.st_mode | stat.S_IXOTH | stat.S_IXGRP |
                        stat.S_IXUSR))
        os.remove("hello.py")

if __name__ == '__main__':
    unittest.main()
