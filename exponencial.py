


def mystery2 (x):
	
	result = x ** 2
	return f'{result}'




number = 5
print(mystery2(number)) 
print('result for mysery 1\n')
print('==========\n')




def second_mystery(list_of_numbers):
	result = 0
	for value in list_of_numbers:
		result += value ** 2
	return result

numberrrrs = [1, 2, 3]
print(f'result for second_mystery {second_mystery(numberrrrs)}')

