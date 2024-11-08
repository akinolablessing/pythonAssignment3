sum = 0
number=int(input("Enter a number:"))
for count in range(1,11,1):
  sum = count*number
  print(f"{count} * {number} = {sum}")