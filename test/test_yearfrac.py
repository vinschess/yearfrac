import unittest
from yearfrac import yearfrac
from datetime import datetime


class Test_Yearfrac(unittest.TestCase):

    def test1(self):
        d1 = datetime(2018, 12, 15)
        d2 = datetime(2019, 3, 1)
        x = yearfrac(d1, d2, 'act')
        self.assertEquals(round(x, 8), 0.20547945)

    def test2(self):
        d1 = datetime(2018, 12, 15)
        d2 = datetime(2019, 3, 1)
        x = yearfrac(d1, d2, 'act_isda')
        self.assertEquals(round(x, 8), 0.20547945)


# run
if __name__ == '__main__':
    unittest.main()
