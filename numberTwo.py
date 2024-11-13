from unittest import TestCase
import numbers

class TestTwoIntegers(TestCase):
	def test_two_integer_exists(self):
		numbers.get_multiply(2)
	def test_two_integer_return_corrects_value(self):
		actual = numbers.get_multiply(2)
		expected = 4
		self.assertEqual(actual,expected)
		