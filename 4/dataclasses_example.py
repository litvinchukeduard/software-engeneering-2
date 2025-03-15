from decimal import Decimal
from dataclasses import dataclass
'''
Написати систему, яка буде керувати апаратом для продажу снеків
'''

# Products, VendingMachine

# Snack, Drink, Candy

# raise ValueError("Hello")


class VendingMachineError(Exception):
    pass


class DuplicateProductError(VendingMachineError):
    pass


class ProductFromOutsideError(VendingMachineError):
    pass


@dataclass(eq=False, frozen=True)
class Product:
    name: str
    price: int

    def calculate_price(self, money):
        return self.price * money
    # def __init__(self, name: str, price: int):
    #     self.name = name
    #     self.price = price

    # def __repr__(self):
    #     return str(self)

    # def __str__(self):
    #     return f"{self.__class__.__name__}({self.name}, {self.price})"
    

class Candy(Product):
    ...
    # def __str__(self):
    #     return f"Candy({self.name}, {self.price})"


class Drink(Product):
    ...


class Snack(Product):
    ...


class VendingMachine:
    # def __init__(self, products={}):
    def __init__(self):
        self.products = {}

        '''
        'Korivka'
        1) Перевірити чи такий продукт вже є
        2.1) Додаємо до списку продуктів
        2.2) Створюємо список з продуктів, а потім додаємо
        '''

        '''
        {
            'Korivka': [<>, <>, <>],
            'Fanta': [<>, <>, <>]
        }
        '''

        self.current_product_count = {
            Candy: 0,
            Drink: 0,
            Snack: 0
        }

        self.max_product_counts = {
            Candy: 2,
            Drink: 2,
            Snack: 2
        }

        # self.current_product_count = {
        #     'Candy': 2,
        #     'Drink': 0,
        #     'Snack': 0
        # }

        # self.max_product_counts = {
        #     'Candy': 2,
        #     'Drink': 2,
        #     'Snack': 2
        # }

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise ValueError("Can only add Product and subclasses to machine")

        product_class = product.__class__
        if self.current_product_count[product_class] == self.max_product_counts[product_class]:
            raise ValueError("Can not add more products of this type")

        self.current_product_count[product_class] += 1
        # print(self.current_product_count)

        # if product.name in self.products:
        #     if product not in self.products[product.name]:
        #         self.products[product.name].append(product)
        #         return
        #     raise ValueError("Duplicate product in system")
        
        # else:
        #     self.products[product.name] = []

        if product.name not in self.products:
            self.products[product.name] = []
        
        if product not in self.products[product.name]:
            self.products[product.name].append(product)
            return
        raise ValueError("Duplicate product in system")
        

        # if product not in self.products:
        #     # self.products.append(product)
            
        #     return
        # raise ValueError("Duplicate product in system")
    
    def __buy_product(self, product: Product, money: int) -> Product:
        if product.name not in self.products \
            or product not in self.products[product.name]:

            raise ValueError("Can not sell product from outside")

        if product.price == money:
            # self.products.remove(product)
            self.products[product.name].remove(product)
            return product
        raise ValueError("Please enter correct amount of money")
    
    def buy_product_using_name(self, name: str, money: int):
        if name not in self.products or len(self.products[name]) == 0:
            raise ValueError(f"Product with name {name} is not present in machine")
        
        product = self.products[name][0]
        self.__buy_product(product, money)

    # def add_product(self, product: Product):

    #     # if isinstance(product, Candy):
    #     #     self.current_product_count['Candy'] 
    #     # elif isinstance(product, Drink):
    #     #     self.current_product_count['Drink']
    #     match product:
    #         case Snack():
    #             print("snack")
    #         case Drink():
    #             print("drink")
    #         case Candy():
    #             print("candy")
    #         case _:
    #             print("Default")

    #     if product not in self.products:
    #         self.products.append(product)
    #         return
    #     raise ValueError("Duplicate product in system")

    # def __init__(self):
    #     self.products = []
        

# print(Drink)

product_one = Candy("Korivka", 10)
# product_one.name = "Hello"
product_two = Drink("Fanta", 30)
# product_three = Candy("Chervony Mak", 10)
product_four = Candy("Korivka", 10)
# product_three = Drink("fanta", 30)

product_five = Drink("Cola", 30)

my_list = [product_one, product_two]

# print(product_one.__class__.__name__)

# my_list.remove(product_one)
# print(my_list)

# my_set = {1, 1, 1, 2, 2}
# print(my_set)

# vending_machine = VendingMachine(my_list)
vending_machine = VendingMachine()
vending_machine.add_product(product_one)
# vending_machine.add_product(product_one)
# vending_machine.add_product(product_one)
# vending_machine.add_product(product_one)
vending_machine.add_product(product_two)
# vending_machine.add_product(product_three)
vending_machine.add_product(product_four)
# vending_machine.add_product("hello")
# vending_machine.add_product(product_four)
print(vending_machine.products)

vending_machine.buy_product_using_name('Korivka', 10)
print(vending_machine.products)

# print(vending_machine.buy_product(product_five, 30))
# print(vending_machine.products)

# print(dir(vending_machine))

# vending_machine._VendingMachine__buy_product(product_five, 30)
# my_int_list = [1, 2, 3, 4]
# my_int_list.remove(2)
# print(my_int_list)
# print(3 in my_int_list)

# print(product_one)
# print(product_two)

# print(product_one == product_two)
# print(product_one)

# print(dir("hello"))
# print(dir(product_one))


# print(Decimal('0.1') + Decimal('0.2'))
# print(0.1 + 0.2)

# self.current_product_count = {
#     'Candy': 2,
#     'Drink': 0,
#     'Snack': 0
# }

# self.max_product_counts = {
#     'Candy': 2,
#     'Drink': 2,
#     'Snack': 2
# }

# 'Candy'
# 'Candy'
# 'Candy' Cannot

# my_str = "addada"

# match my_str:
#     case "World":
#         print("world")
#         # break
#     case "Hello":
#         print("hello")
#     case "People":
#         print("people")
#     case _:
#         print("Default")

# candy_dict = {'Korivka': [], 'Chervony Mak': []}
# print('Fanta' in candy_dict)

try:
    ...


except DuplicateProductError:
    print("Please do not enter duplicate products")
except VendingMachineError:
    print("Sorry, Machine is out of order")

