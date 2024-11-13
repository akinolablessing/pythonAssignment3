from unittest import TestCase
import numbers

class TwoNumbers(TestCase):
	def Two_Numbers_exists(self):
		numbers.get_multiply(2)
	def Two_Numbers_return_corrects_value(self):
		actual = numbers.get_multiply(2)
		expected = 4
		self.assertEqual(actual,expected)
		actual = numbers.get_multiply(5)
		expected = 10
	self.assertEqual(actual,expected)
        def test_that_Two_Numbers_raise_exception_with_invalid_input(self)
		self.assertRaises(TypeError, numbers.get_multiply, "Ayomide")
	def test_that_Two_Numbers_returns_correct_value_with_int(self)
		actual = numbers.get_multiply(4)
		expected = 4
		self.assertEqual(actual, expected)




