import unittest
from accy.accy_functions import cpd_int

class AccyFunctions(unittest.TestCase):
    def test_accy_functions(self):
        exp = 8235.05
        p = 5000
        r = 0.05
        n = 12
        t = 10
        out = cpd_int(p, r, n, t)
        self.assertAlmostEqual(exp, out, 2)

if __name__ == "__main__":
    unittest.main()
