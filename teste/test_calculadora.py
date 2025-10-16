import unittest
import cal

class testCalc(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(cal.soma(10,10), 20)
        self.assertEqual(cal.soma(-5,10), 5)
        self.assertEqual(cal.soma(30,10), 40)


    def test_subtrair(self):
        self.assertEqual(cal.subtrair(-55,60), 5)


if __name__=="__main__":
    unittest.main()       


