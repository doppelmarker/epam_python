class Customer:
    attr = "Python is awesome!"

    def __init__(self, first_name):
        self.first_name = first_name

    def __del__(self):
        print("I was not deleted!")


cust1 = Customer("customer1")
cust2 = Customer("customer2")

print(cust1.__dict__, cust2.__dict__)
print(cust1.attr, cust2.attr)

cust1.attr = "MEEEMEMEMEMEMME"
print(Customer.__dict__, cust1.__dict__, cust2.__dict__)
print(cust1.attr, cust2.attr)

del cust1.attr

Customer.attr = "!!!!!!!!!!!!!!"
print(Customer.__dict__, cust1.__dict__, cust2.__dict__)
print(cust1.attr, cust2.attr)
