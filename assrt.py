from unittest import TestCase
from divisionNumbers import number_divi_division

class NumbersDivider(TestCase):
	def test_numbers_divider_exists(self):
		number_divi_division(2,2)
		actual = number_divi_division(2,2)
		expected = 1
	self.assertEqual = (actual , expected)
		
		
	