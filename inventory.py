# Lesson SE-T32
# Task  Capstone Project IV-OOP


# Define class named Shoe.
class Shoe:

    # Initialize the objects attributes.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Methode for returning the cost of a shoe.        
    def get_cost(self):
        return self.cost

    # Methode for returning the quantity if the shoes.
    def get_quantity(self):
        return self.quantity

    # Method to return a string representation of the class. 
    def __str__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"


# A list to store a list of objects of shoes.
shoe_list = []


# A function that reads the inventory file, creates shoe objects from the data
#   and appends the ojects into the shoe list.
def read_shoes_data():

    try:
        with open("inventory.txt", "r") as inventory:
            row = 0
            try:
                for line in inventory:
                    if row != 0:
                        line = line.strip("\n")
                        line = line.split(",")
                        country = line[0]  
                        code = line[1]
                        product = line[2]
                        cost = line[3]
                        quantity = line[4]
                        shoe = Shoe(country, code, product, cost, quantity)
                        shoe_list.append(Shoe(country, code, product, cost, quantity))
                        row += 1
                    else:
                        row += 1

            except IndexError:
                print(""" 
                        *** There is a format error in the inventory file! *** 
                                     Please check the text file.
                                                                            """)

            except SyntaxError:
                print(""" 
                        *** There is a format error in the inventory file! *** 
                                     Please check the text file.
                                                                            """)
            
    except FileNotFoundError:
        print("\n\t\t*** The inventory file does not exist! ***\n")
        exit()
   

# A function to allow the user to add a new shoe model which will be added to the list
#   of shoe objects and update the inventory file.
def capture_shoes():
    print("\n\t\t\t\t*** Add new shoe to the warehouse ***\n")
    country = input("\n\t\t\t\t\tCountry: ")
    code = input("\n\t\t\t\t\tCode: SKU")
    product =input("\n\t\t\t\t\tProduct: ")
    cost = input("\n\t\t\t\t\tCost: ")
    quantity = input("\n\t\t\t\t\tQuantity: ")
    shoe = Shoe(country, "SKU" + code, product, cost, quantity)
    shoe_list.append(Shoe(country, "SKU" + code, product, cost, quantity))

    with open("inventory.txt", "a") as inventory:
        inventory.write(f"{country},SKU{code},{product},{cost},{quantity}\n")
    

# A function that iterates over the shoes list and prints the details 
#   of the shoes returned from the __str__ function. 
def view_all():
    print("\n\n\t\t\t    Country Code Product Cost Quantity\n")

    for shoe in shoe_list:
        print("\t\t\t   ", shoe)
        
    print()

    
# This function finds the shoe object with the lowest quantity,
#   which is the shoes that needs to be re-stocked, asks the user how
#   many shoes to add to the stock and updates the inventory file.   
def re_stock():
    count = []

    try:
        for shoe in shoe_list:
            count.append(int(shoe.quantity))
        
        for shoe in shoe_list:
            if int(shoe.quantity) == min(count):
                print("\n\t\t\t    Lowest stock:", shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity)
                add_stock = input("\t\t\t    How many shoes would you like to add: ")
                shoe.quantity = int(add_stock) + int(shoe.quantity)
                print("\n\t\t\t   ", shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity)
               
                with open("inventory.txt", "w") as inventory:
                    inventory.write("Country,Code,Product,Cost,Quantity\n")
                    for shoe in shoe_list:
                        inventory.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

    except ValueError:
        print(""" 
                        *** There are missing values in the inventory file! *** 
                                      Please check the text file.
                                                                            """)

 
# This function searches for a shoe from the list using the shoe code 
#   and returns this object so that it will be printed.
def search_shoe():
    print("\n\t\t\t\t *** Search for a shoe in stock ***")
    sku = input("\n\t\t\t\t Please enter the Code: SKU") 
    print("\n\n\t\t\t    Country Code Product Cost Quantity\n")

    for shoe in shoe_list:
        if sku in shoe.code:
            print("\t\t\t   ", shoe, "\n")
        

# This function calculates the total value for each item and prints this
#    information on the console for all the shoes.
def value_per_item():
    print("\n\n\t\t\t    The total value of each item in stock:\n")

    try:
        for shoe in shoe_list:
            value = int(shoe.cost) * int(shoe.quantity)
            print("\t\t\t   ", shoe.product, "is", value)
    
        print()

    except ValueError:
        print(""" 
                        *** There are missing values in the inventory file! *** 
                                      Please check the text file.
                                                                            """)


# This function determines the product with the highest quantity and
#   prints this shoe as being for sale.
def highest_qty():
    count = []

    try:
        for shoe in shoe_list:
            count.append(int(shoe.quantity))
    
        for shoe in shoe_list:
            if int(shoe.quantity) == max(count):
                print("\n\t\t\t    On Sale: ", shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity)

    except ValueError:
        print(""" 
                        *** There are missing values in the inventory file! *** 
                                      Please check the text file.
                                                                        """)
        
    
#==========Main Menu=============
read_shoes_data()
user_choice = 0

while user_choice != "7":
    print("""
                            __________________________________________

                            Please choose one of the following options

                            1   Re-stock shoes
                            2   Display the highest quantity of shoes
                            3   Add a new model  
                            4   Display value of each shoe model
                            5   Search for a shoe model
                            6   View all shoes

                            q   To quit the program 
                            __________________________________________
                                                                        """)

    user_choice = input("\t\t\t\t  Please enter your choice: ")

    if user_choice == "1":
        re_stock()

    elif user_choice == "2":
        highest_qty()  
    
    elif user_choice == "3":
        capture_shoes()       

    elif user_choice == "4":
        value_per_item()

    elif user_choice == "5":
        search_shoe()

    elif user_choice == "6":
        view_all()

    elif user_choice == "q":
        print("\n\n\t\t\t\t\t*** Goodbye! ***\n")
        break

    else:
        print("\n\t\t\t\t*** Option is not available ***")
        continue 

