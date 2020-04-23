import unittest

loader = unittest.TestLoader()
suites = loader.discover(".", pattern="*_test.py")

print("start")  # Don't remove this line

for suite in suites._tests:
    for cls in suite._tests:
        try:
            for m in cls._tests:
                print(m.id())
        except Exception as e:
            print(e)
            pass