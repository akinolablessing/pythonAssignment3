def midnight(value):
	result = 0
	for count in value:
		result += count**5
	return result
number = [13]
print(midnight(number))