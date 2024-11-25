def jessica_menu():
	print("""
        ~~~~Main Menu~~~~
          1.View Products
          2.Add to Cart
          3.Remove from Cart
          4.View Cart
          5.CheckOut
          6.Exist
""")
	print(f"you have {len(cart[0])} items")
	select = int(input(">>>"))
	match select:
		case 1:View_products()
		case 2:Add_to_cart()
		case 3:Remove_from_cart()
		case 4:Check_out()
		case 5:Print("exiting")

def view_products():
	for count in range (len(products[0])):
		print(f"{count + 1}. {products[0][count]}   {products[1][index]}")
	print("""
  do you want to go back?
  1.back
""")
	select = int(input(">>>"))
	match select:
		case 1:jessica_menu()

def add_to_cart():
	for count in range(len(products[0])):
		print(f"{count + 1}. {products[0][count]}  {products[1][count]}")
	select = int(input("add to cart\n >>>"))
	cart[0].append(products[0][select -1])
	cart[1].append(products[1][select -1])
	print(f"{products[0][select -1]} has been added to cart....")
	jessica_menu()	

def check_out():
	total = 0
	for count in range (len(cart[0])):
		total += cart[1][count]
		print(f"{count + 1}. {cart[0][count]}  {cart[1][count]}")
	print(f"the total price is: {total}")
	cart[0].clear()
	cart[1].clear()
	select = input("would you like to go back to main? yes / no:")
	if select.lower() == "yes":
		jessica_menu()
	else:
		print("thank you for shopping with us....")

def remove_from_cart():
	for count in range(len(cart[0])):
		print(f"{count + 1}.  {cart[0][count]}")
	select = int(input(">>>"))
	if len(cart) == 2:
		cart[0].pop([0][select - 1])
		cart[1].pop([0][select - 1])
		jessica_menu()
	else:
		print("no count")


select = [["Laptop ", "Phone" ,"Headphones"] , [1000 , 500 , 100]]
cart = [[] , []]
jessica_menu()
		
		



		