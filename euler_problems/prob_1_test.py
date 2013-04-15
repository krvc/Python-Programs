import prob_1
import unittest

class Prob_1UnitTests(unittest.TestCase):

    def test_negative_arguments(self):
        self.assertFalse(prob_1.mult(-3))
        self.assertFalse(prob_1.mult(-5))
    
    def test_passing_non_multiples_of_three_or_five(self):
        self.assertFalse(prob_1.mult(2))
        self.assertFalse(prob_1.mult(4))
    
    def test_multiples_of_three(self):
        
        multiples_of_three = [x for x in range(1, 1000) if x % 3 == 0]

        for e in multiples_of_three:
            self.assertTrue(prob_1.mult(e))
    
    def test_multiples_of_three(self):
        
        multiples_of_three = [x for x in range(1, 1000) if x % 5== 0]

        for e in multiples_of_three:
            self.assertTrue(prob_1.mult(e))
        
if __name__ == '__main__':
    unittest.main()
        
