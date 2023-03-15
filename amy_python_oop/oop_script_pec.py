# design at least 3 classes: person, employee and customer
# consider appropriate constructors, properties and methods for these classes
# demonstrate understanding of encapsulation, inheritance and polymorphism
# create a client script and instantiate objects based on the above classes
# and call their methods and set their properties to demo working fucntionality

# from person import Person

from employee import Employee

from customer import Customer

employee1 = Employee("Jane Bloggs", "140682", "FK7 7SN", "01012015", "12345", 35000)
employee2 = Employee("Joe Banks", "010184", "YO6 3EB", "01012020", "12346", 32000)
customer1 = Customer("Emma Crisp", "010285", "RH4 3BA", 1, "Y", 204)
customer2 = Customer("Sue Gray", "050386", "RH3 8LT", 3, "N", 6)

# employee1.set_department("sales")
# employee2.set_pension_date("140222")
# customer1.set_points(2560)
# customer2.set_points(300)
#
# # create customer list and append customer name to it NB won't like this as access to a protected characteristic
# customers = []
# customers.append(customer1._name)
# customers.append(customer2._name)
# for e in customers:
#     print(e)
#
#
# employee1.set_mobile("07771826401")
# print(employee1._name) #doesn't like this as in init file?
#
# # set points balance for different customers
# customer1.set_points(2560)
# customer2.set_points(300)
#
# # check whether customers can redeem their points
# customer2.check_points()
# customer1.check_points()
#
# employee1.check_pension_elig()

# demonstrates inheritance as is method from person
employee1.set_mobile(447801825780)
employee1.get_mobile()

customer2.set_points(2500)
customer2.check_points()

# employee1.set_country("Scotland")
# customer1.set_country("Wales")

# adding an attribute to a list
employee_country = []
employee2.set_country("UK")
employee1.set_country("Spain")
customer1.set_country("Iceland")
customer2.set_country("UK")
employee_country.append(employee1.get_country())
employee_country.append(employee2.get_country())

# printing out the list of countris
for e in employee_country:
    print(e)

# running if statement on object attribute using class and passing instance as argument
if Employee.get_country(employee1) == "Spain":
    print("You're eligible for Zara discount")
else:
    print("No discounts for you")

# or can use instance in first instance
if customer2.get_country() == "UK":
    print("You're in the UK")
else:
    print("You're outside UK")
