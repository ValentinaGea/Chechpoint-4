from decimal import Decimal
import math

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
my_list = ['a', 'b', 'c', 'd']
my_tuple = (104, 56, 5, 324)
my_float = 12.67
my_integer = 100
my_decimal = Decimal('5.65')
my_dictionary = {
  'nombre': 'Alison',
  'edad': 30,
  'ciudad': 'Vitoria-Gasteiz'
}

# Exercise 2: Round your float up.
my_round_up = math.ceil(my_float)
print(my_round_up)

# Exercise 3: Get the square root of your float.
my_square_root = math.sqrt(my_float)
print(my_square_root)

# Exercise 4: Select the first element from your dictionary.
first_key = next(iter(my_dictionary))
first_valor = my_dictionary[first_key]
print(first_key)
print(first_valor)

# Exercise 5: Select the second element from your tuple.
second_elem = my_tuple[1]
print(second_elem)

# Exercise 6: Add an element to the end of your list.
my_list.append('e')
print(my_list)

# Exercise 7: Replace the first element in your list.
my_list[0] = ('w')
print(my_list)

# Exercise 8: Sort your list alphabetically.
my_list.sort()
print(my_list)

# Exercise 9: Use reassignment to add an element to your tuple.
my_tuple += (10,)
print(my_tuple)