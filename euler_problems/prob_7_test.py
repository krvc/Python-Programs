import unittest
import prob_7

class Prob_7UnitTests(unittest.TestCase):
    def test_integers_only(self):
        self.assertRaises(TypeError, prob_7.isprime, 1.0, 7)
        self.assertRaises(TypeError, prob_7.isprime, 1, 7.0)
        self.assertRaises(TypeError, prob_7.isprime, 1.0,7.0)
        self.assertRaises(TypeError, prob_7.isprime, 1.0, [7])
        
    def test_below_1(self):
        self.assertRaises(ValueError,prob_7.isprime, 0) 
        
        
if __name__ == '__main__':
    unittest.main()   
           
