import sys
import unittest
from tests.test_dummy_03 import TestDummy03
from tests.test_dummy_02 import TestDummy02


def suite():
    suite1 = unittest.TestSuite()
    suite1.addTest(unittest.makeSuite(TestDummy03))
    suite1.addTest(unittest.makeSuite(TestDummy02))
    return suite1


def run():
    loader = unittest.defaultTestLoader
    loader.sortTestMethodsUsing = None
    result = unittest.TextTestRunner(loader, verbosity=2).run(suite())
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    run()
