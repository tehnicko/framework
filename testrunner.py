import sys
import unittest
from tests.test_dummy_01 import TestDummy01
from tests.test_dummy_02 import TestDummy02
from tests.test_dummy_03 import TestDummy03


def suite():
    # test_list = [TestDummy02, TestDummy01]
    # test_load = unittest.TestLoader()
    #
    # testlist = []
    # for testCase in test_list:
    #     test_suite = test_load.loadTestsFromTestCase(testCase)
    #     testlist.append(test_suite)
    #
    # suite_x = unittest.TestSuite(testlist)
    # return suite_x

    suite_x = unittest.TestSuite()
    suite_x.addTest(unittest.makeSuite(TestDummy02))
    suite_x.addTest(unittest.makeSuite(TestDummy03))
    suite_x.addTest(unittest.makeSuite(TestDummy01))

    return suite_x


def run():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == '__main__':
    unittest.defaultTestLoader.sortTestMethodsUsing = None
    # unittest.main(defaultTest='suite')
    run()
