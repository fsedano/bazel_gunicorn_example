import time
import unittest

from svc1.src.f1 import Suma

class BasicTestCase(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(1,1)

    def test_suma(self):
        
        for x in range(1,100):
            res = Suma(1,x)
            self.assertEqual(res, x+1)

if __name__ == "__main__":
    import pytest
    import sys

    sys.exit(pytest.main([__file__]))