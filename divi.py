from unittest import TestCase
from divisionNumbers import number_divi_division

class TwoNumbers(TestCase):
	def test_two_Numbers_exists(self):
		number_divi_division(10, 2)
	def test_two_Numbers_return_corrects_value(self):
		actual = number_divi_divition(10, 2)
		expected = 5
		self.assertEqual(actual,expected)
		actual = number_divi_division(10, 5)
		expected = 2
		self.assertEqual(actual,expected)
	def test_that_Two_Numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, number_to_division, "Ayomide")
	def test_that_Two_Numbers_returns_correct_value_with_int(self):
		actual = number_divi_division(4, 2)
		expected = 2
		self.assertEqual(actual, expected)


