from unittest import TestCase
import numberTwoo

class TestTwoNumbers(TestCase):
	def test_two_numbers_exists(self):
		numberTwoo.get_multiply(2,2)
	def test_two_numbers_return_corrects_value(self):
		actual = numberTwoo.get_multiply(2,2)
		expected = 4
		self.assertEqual(actual,expected)
		