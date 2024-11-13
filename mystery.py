def mystery(numbers):
	result = 0
	for value in numbers:
		result += value **2
	return result
number = [1,2,3,4,5]
print(mystery(number))