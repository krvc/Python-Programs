import unittest
import prob_3

class Prob_3UnitTests(unittest.TestCase):    
    
    def test_must_be_2_or_greater(self):
        #number must be 2 or greater
        self.assertRaises(ValueError, prob_3.prim_fact, -3)
        self.assertRaises(ValueError, prob_3.prim_fact, -2)
        self.assertRaises(ValueError, prob_3.prim_fact, -1)
        self.assertRaises(ValueError, prob_3.prim_fact, 0)
    
    def test_known_composites(self):
        self.assertEqual(prob_3.prim_fact(4), [2, 2])
        self.assertEqual(prob_3.prim_fact(6), [2, 3])
        self.assertEqual(prob_3.prim_fact(9), [3, 3])
        self.assertEqual(prob_3.prim_fact(10), [2, 5])
        self.assertEqual(prob_3.prim_fact(12), [2, 2, 3])
        self.assertEqual(prob_3.prim_fact(14), [2, 7])
        self.assertEqual(prob_3.prim_fact(15), [3, 5])
        
    def test_prime_number_input(self):
        #behaves well when input is prime number
        self.assertEqual(prob_3.prim_fact(2), [2])
        self.assertEqual(prob_3.prim_fact(3), [3])
        self.assertEqual(prob_3.prim_fact(5), [5])
        self.assertEqual(prob_3.prim_fact(7), [7])
        self.assertEqual(prob_3.prim_fact(11), [11])
        self.assertEqual(prob_3.prim_fact(13), [13])
        self.assertEqual(prob_3.prim_fact(17), [17])
if __name__ == '__main__':
    unittest.main()
