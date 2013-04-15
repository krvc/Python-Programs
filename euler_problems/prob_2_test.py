import prob_2
import unittest

class Prob_1UnitTests(unittest.TestCase):
    def test_integer_parameter(self):
        #fibo should only accept integer parameters
        self.assertRaises(TypeError, prob_2.fibo, "10")
        self.assertRaises(TypeError, prob_2.fibo, 10.0)
        self.assertRaises(TypeError, prob_2.fibo, [10])
        
    def test_positive_parameter(self):
        #fibo parameter must be greater than 1
        self.assertRaises(prob_2.NoElementsBelowGivenParameter,
                          prob_2.fibo, 0)
        self.assertRaises(prob_2.NoElementsBelowGivenParameter,
                          prob_2.fibo, 1)
        self.assertRaises(prob_2.NoElementsBelowGivenParameter,
                          prob_2.fibo, -1)
        self.assertRaises(prob_2.NoElementsBelowGivenParameter,
                          prob_2.fibo, -2)
        self.assertRaises(prob_2.NoElementsBelowGivenParameter,
                          prob_2.fibo, -3)

    def test_known_values(self):
        #fibo should return correct known values
        self.assertEqual(prob_2.fibo(3), [1,2,3])
        self.assertEqual(prob_2.fibo(4), [1,2,3,5])
        
if __name__ == '__main__':
    unittest.main()
        
    
