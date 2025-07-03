# Easy 1
# def isnt_it_odd(value):
#     return abs(value) % 2 != 0


# print(isnt_it_odd(10))
# print(isnt_it_odd(8))
# print(isnt_it_odd(24253))
# print(isnt_it_odd(3333))
# print(isnt_it_odd(0))

# def odd_numbers():
#     for n in range(100):
#         if n % 2 != 0:
#             print(n)

# odd_numbers()

# def even_numbers():
#     for n in range(100):
#         if n % 2 == 0:
#             print(n)

# even_numbers()

# def area_of_room():
#     length = input("what is the length?")
#     width = input("what is the width?")
#     area = int(length) * int(width)

#     return f"Square meters is: {area} and square feet is {area*10.7639}"

# print(area_of_room())

# def tip_calculator():
#     bill = float(input("How much was the bill?"))
#     tip_rate = float(input("How much is the tip rate?"))/100

#     tip = bill * tip_rate
#     total = bill + tip

#     return f"The tip is ${tip:.2f} and \n the total is ${total:.2f}"

# print(tip_calculator())

# def sum_or_product():
#     number = int(input("Enter a integer greater than 0"))

#     choice = input('Enter "s" to compute sum or enter "p" to compute product')

#     if choice == "s":
#         sum = 0
#         for n in range(1, number + 1):
#             sum += n
#         return f"The sum of integers between 1 and {number} is {sum}"
#     elif choice == "p":
#         product = 1
#         for n in range(1, number + 1):
#             product *= n
#         return f"The product of integers between 1 and {number} is {product}"
#     else:
#         return "Thats not one of the inputs"

# print(sum_or_product())

# def short_long_short(string1, string2):
#     if len(string1) > len(string2):
#         return string2 + string1 + string2
#     else:
#         return string1 + string2 + string1

# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# def is_leap_year(year):
#     if year < 1752 and year % 4 == 0:
#         return True
#     elif year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     else:
#         return year % 4 == 0

# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# def multisum(number):
#     sum = 0
#     for i in range(1, number + 1):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum

# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# def utf16_value(string):
#     sum = 0
#     for char in string:
#         sum += ord(char)

#     return sum

# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# ----------------------------------------Easy 2---------------------------------------- #

# def greetings(name, job):
#     return(f"Hello, {' '.join(name)}! Nice to have a "
#            f"{job['title']} {job['occupation']}"
#            " around.")

# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
def greet():
    greeter = input("What is your name? ")
    if greeter[len(greeter) -1] == "!":
        return (f"HELLO {greeter}! WHY ARE WE YELLING?")
    return f"Hello {greeter}"
