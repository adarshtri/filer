import unittest
import sys
from distutils.util import get_platform


class NewFeatureTest(unittest.TestCase):

    def test_sysversion(self):
        self.assertGreaterEqual(sys.version_info, (3, 6))

    def test_platform(self):
        platform = get_platform()
        self.assertIn("linux", platform)


if __name__ == '__main__':
    unittest.main()
