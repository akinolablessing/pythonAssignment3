num = int(input("Enter  number:"))
sum = int(num/10000)%10 , int(num/1000)%10, int(num/100)%10, int(num/10)%10, num%10
print(sum)