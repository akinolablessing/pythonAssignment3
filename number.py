from unittest import TestCase
import numberTwo

class TestTwoNumbers(TestCase):
	def test_two_numbers_exists(self):
		numberTwo.get_multiply(2,2)
	def test_two_numbers_return_corrects_value(self):
		actual = numbersTwo.get_multiply(2,2)
		expected = 4
		self.assertEqual(actual,expected)
		

