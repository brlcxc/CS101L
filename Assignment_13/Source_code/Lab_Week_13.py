########################################################################
##
## CS 101 Lab
## Program Week 13
## Name Bishop Lohman
## Email brlcxc@umsystem.edu
##
## Algorithm:
# 1. A test is run on total to see if the total of [1,10,22] is 33
# 2. A test is run on total to see if the total of [] is 0
# 3. A test is run on average to see if the average of [2,5,9] is 5.333…
# 4. A test is run on average to see if the average of [2,15,22,9] is 12
# 5. A test is run on average to see if the average of [] is math.nan
# 6. A test is run on median to see if the median of [2,5,1] is 2
# 7. A test is run on median to see if the median of [5,2,1,3] is 2.5
# 8. A test is run on median to see if ValueError is raised when [] is input
## Error Handling:
# The function itself will output an error messgae if a unit test is not passed
## Other Comments:
# All unit test methods must start with the name 'test'
##
########################################################################

import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result, 33, 'The total function should return 33')

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 0')

    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result, 5.3333, 4, 'The average function should return 5.33333')

    def test_average_two(self):
        result = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result, 12.0000, 4, 'The average function should return 5.33333')

    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(result, math.nan, 'The average function should return math.nan')

    def test_median_one(self):
        result = Grades.median([2,5,1])
        self.assertEqual(result, 2, 'The median function should return 2')

    def test_median_two(self):
        result = Grades.median([5,2,1,3])
        self.assertEqual(result, 2.5, 'The median function should return 2.5')

    def test_median_raise_ValueError(self):
        with self.assertRaises(ValueError):
                result = Grades.median([])

unittest.main()