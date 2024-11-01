library=int(input("Enter the number of days the member is late to return the book: "))
if(library<=5):
    print("fine is 50 paise")
elif(library=6):
    print("fine is one rupee")
elif(library>=10):
    print("Fine is 5 rupees")
elif(library>30):
    print("Your membership will be cancelled")