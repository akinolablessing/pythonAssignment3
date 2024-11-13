from unittest import TestCase
from divisionNumbers import number_integer_division

class NumbersDivider(TestCase):
	def test_numbers_divider_exists(self):
		number_integer_division(2,2)
		actual = number_division(2,2)
		expected = 1
		self.assertEqual = (actual , expected)
	def test_numbers_divider_exists(self):
		number = number_division(10,2)
		actual = number_division(10,2)
		expected = 5
		self.assertEqual = (actual , expected)

	