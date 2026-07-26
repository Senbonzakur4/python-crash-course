# 5.1. Conditional Tests

ingredients = ['banana', 'flour', 'sugar', 'eggs', 'milk', 'chocolate chips', 
               'baking powder', 'vanilla extract', 'salt']

nums = [2, 4, 5, 7, 8, 10]
ingredient1 = 'banana'
ingredient2 = 'EgGs'
num1 = 0
num2 = 1
num3 = 9

print(f"\nIs 'ingredient' == 'banana'? I predict True.")
print(ingredient1 == 'banana')

print(f"\nIs 'ingredient' == 'flour'? I predict False.")
print(ingredient2.lower() == 'flour')

print(f"\nIs 'num' == 1? I predict False.")
print(num1 == 1)

print(f"\nIs 'num' != 9? I predict True.")
print(num2 != 9)

print(f"\nIs 'num' > 5? I predict False.")
print(num1 > 5)

print(f"\nIs 'num' < 10? I predict True.")
print(num3 < 10)

print(f"\nIs 'num' >= 9? I predict True.")
print(num3 >= 9)

print(f"\nIs 'num' <= 0? I predict False.")
print(num2 <= 0)

print(f"\nIs 'num' > 5 and 'num' < 10? I predict True.")
print(num3 > 5 and num3 < 10)

print(f"\nIs 'num' < 5 or 'num' > 10? I predict False.")
print(num3 < 5 or num3 > 10)

print(f"\nIs 'soda' in ingredients? I predict False.")
print('soda' in ingredients)

print(f"\nIs 'chocolate chips' not in ingredients? I predict False.")
print('chocolate chips' not in ingredients)