from unittest import TestCase
import numbers

class TestTwoIntegers(TestCase):
	def test_two_integers_exists(self):
		numbers.get_multiply(2,2)
	def test_two_integers_return_corrects_value(self):
		actual = numbers.get_multiply(2,2)
		expected = 4
		self.assertEqual(actual,expected)
		        