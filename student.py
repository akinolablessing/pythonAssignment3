counter = 1
numberOfFailure = 0
numberOfPass = 0

for count in range(3):
 grade = int(input("Enter student's score:"))
 if grade < 50 :
   numberOfFailure+=1
else:
  numberOfPass+=1
  counter+=1

print(f"pass {numberOfPass}")
print(f"faill {numberOfFailure}")
