import sys
import unittest
from tests.test_example_1 import TestDummy01


def suite():
    first_suite = unittest.TestSuite()
    first_suite.addTest(unittest.makeSuite(TestDummy01))

    return first_suite


def run():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == '__main__':
    unittest.defaultTestLoader.sortTestMethodsUsing = None
    # unittest.main(defaultTest='suite')
    run()
