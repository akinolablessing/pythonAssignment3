num=int(input("Enter threeNumber:"))
sum=0
sum1=0
while num > 0:
    sum=num%10
    sum1=sum1+sum
    num=num//10
   
    print(sum1)