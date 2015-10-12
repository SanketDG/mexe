#!/usr/bin/env python
import os
import stat
import unittest

import mexe


class TestHelperFunctions(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        os.remove("hello.py")

    def test_contains_shebang_default(self):
        with open("hello.py", 'wb+') as f:
            mexe.put_shebang(f, version='default')
        with open("hello.py", 'rb') as f:
            self.assertTrue(mexe.contains_shebang(f, version='default'))

    def test_contains_shebang_python2(self):
        with open("hello.py", 'wb+') as f:
            mexe.put_shebang(f, version='2')
        with open("hello.py", 'rb') as f:
            self.assertTrue(mexe.contains_shebang(f, version='2'))

    def test_contains_shebang_python3(self):
        with open("hello.py", 'wb+') as f:
            mexe.put_shebang(f, version='3')
        with open("hello.py", 'rb') as f:
            self.assertTrue(mexe.contains_shebang(f, version='3'))

    def test_contains_shebang_python_bad_version(self):
        with open("hello.py", 'wb+') as f:
            mexe.put_shebang(f, version='default')
        with open("hello.py", 'rb') as f:
            self.assertRaises(KeyError, mexe.contains_shebang, f, '4')

    def test_not_contains_shebang(self):
        with open("hello.py", 'wb+') as f:
            f.seek(0)
            f.write(b"some random text")
        with open("hello.py", 'rb') as f:
            self.assertFalse(mexe.contains_shebang(f, version='default'))
        # os.remove("hello.py")

    def test_put_shebang_default(self):
        with open("hello.py", "wb+") as f:
            mexe.put_shebang(f, version='default')
        with open("hello.py", 'rb') as f:
            self.assertEqual(f.readline(), mexe.shebangs['default'])

    def test_put_shebang_python2(self):
        with open("hello.py", "wb+") as f:
            mexe.put_shebang(f, version='2')
        with open("hello.py", 'rb') as f:
            self.assertEqual(f.readline(), mexe.shebangs['2'])

    def test_put_shebang_python3(self):
        with open("hello.py", "wb+") as f:
            mexe.put_shebang(f, version='3')
        with open("hello.py", 'rb') as f:
            self.assertEqual(f.readline(), mexe.shebangs['3'])

    def test_put_shebang_python_bad_version(self):
        with open("hello.py", "wb+") as f:
            self.assertRaises(KeyError, mexe.put_shebang, f, '4')

    def test_make_exec(self):
        mexe.make_exec("hello.py", version='default')
        st = os.stat("hello.py")
        self.assertTrue(bool(st.st_mode | stat.S_IXOTH | stat.S_IXGRP |
                             stat.S_IXUSR))

if __name__ == '__main__':
    unittest.main()
