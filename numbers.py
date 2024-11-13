from unittest import TestCase
from multiplyNumbers import number_to_multiply

class TwoNumbers(TestCase):
	def test_two_Numbers_exists(self):
		number_to_multiply(2, 2)
	def test_two_Numbers_return_corrects_value(self):
		actual = number_to_multiply(2, 2)
		expected = 4
		self.assertEqual(actual,expected)
		actual = number_to_multiply(5, 2)
		expected = 10
		self.assertEqual(actual,expected)
	def test_that_Two_Numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, number_to_multiply, "Ayomide")
	def test_that_Two_Numbers_returns_correct_value_with_int(self):
		actual = number_to_multiply(4, 1)
		expected = 4
		#self.assertEqual(actual, expected)




