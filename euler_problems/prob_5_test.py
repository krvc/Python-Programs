import unittest
import prob_5

class Prob_3UnitTests(unittest.TestCase): 
    def test_known_values(self):
        self.assertEqual(prob_5.leastcomnfact(1, 1), 1)
        self.assertEqual(prob_5.leastcomnfact(1, 2), 2)
        
    def test_integers_only(self):
        self.assertRaises(TypeError, prob_5.leastcomnfact, 1.0, 7)
        self.assertRaises(TypeError, prob_5.leastcomnfact, 1, 7.0)
        self.assertRaises(TypeError, prob_5.leastcomnfact, 1.0, 7.0)
        self.assertRaises(TypeError, prob_5.leastcomnfact, "1", 7)
        
    def test_below_1(self):
        self.assertRaises(ValueError, prob_5.leastcomnfact,  0, 7)
        self.assertRaises(ValueError, prob_5.leastcomnfact, -1, 7)
        self.assertRaises(ValueError, prob_5.leastcomnfact, -2, 7)
        self.assertRaises(ValueError, prob_5.leastcomnfact,  0,-1)
        self.assertRaises(ValueError, prob_5.leastcomnfact, -1, 0)
        

if __name__ == '__main__':
    unittest.main()   
    
