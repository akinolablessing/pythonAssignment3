from unittest import TestCase
import numberTwo

class TwoNumbers(TestCase):
	def Two_Numbers_exists(self):
		numbers.get_multiply(2,2)
	def Two_Numbers_return_corrects_value(self):
		actual = numbers.get_multiply(2,2)
		expected = 4
		self.assertEqual(actual,expected)
		

