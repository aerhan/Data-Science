# 1. Reverse a string
reverse_string = lambda s: s[::-1]

# 2. Check if a string is palindrome
is_palindrome = lambda s: s == s[::-1]

# 3. Count the number of vowels in a string
count_vowels = lambda s: sum(1 for char in s if char.lower() in 'aeiou')

# 4. Flatten a list of lists
flatten_list = lambda lst: [item for sublist in lst for item in sublist]

# 5. Remove duplicates from a list
remove_duplicates = lambda lst: list(set(lst))

# 6. Find the maximum value in a list
max_value = lambda lst: max(lst)

# 7. Find the minimum value in a list
min_value = lambda lst: min(lst)

# 8. Calculate the square of a number
square = lambda x: x**2

# 9. Calculate the cube of a number
cube = lambda x: x**3

# 10. Check if a number is even
is_even = lambda x: x % 2 == 0

# 11. Check if a number is odd
is_odd = lambda x: x % 2 != 0

# 12. Calculate the factorial of a number
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# 13. Find the length of a string
string_length = lambda s: len(s)

# 14. Find the length of a list
list_length = lambda lst: len(lst)

# 15. Capitalize the first letter of each word in a string
capitalize_words = lambda s: ' '.join(word.capitalize() for word in s.split())

# 16. Check if a number is prime
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# 17. Calculate the sum of digits in a number
sum_of_digits = lambda n: sum(int(digit) for digit in str(n))

# 18. Check if a year is a leap year
is_leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 19. Find the nth Fibonacci number
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# 20. Reverse a list
reverse_list = lambda lst: lst[::-1]

# 21. Convert a string to lowercase
to_lowercase = lambda s: s.lower()

# 22. Convert a string to uppercase
to_uppercase = lambda s: s.upper()

# 23. Check if a string starts with a specific substring
starts_with = lambda s, sub: s.startswith(sub)

# 24. Check if a string ends with a specific substring
ends_with = lambda s, sub: s.endswith(sub)

# 25. Check if a list is sorted
is_sorted = lambda lst: all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# 26. Convert temperature from Celsius to Fahrenheit
celsius_to_fahrenheit = lambda celsius: celsius * 9/5 + 32

# 27. Convert temperature from Fahrenheit to Celsius
fahrenheit_to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5/9

# 28. Calculate the area of a rectangle
rectangle_area = lambda length, width: length * width

# 29. Calculate the area of a circle
circle_area = lambda radius: 3.14159 * radius**2

# 30. Calculate the circumference of a circle
circle_circumference = lambda radius: 2 * 3.14159 * radius

# 31. Find the maximum value in a dictionary
max_dict_value = lambda d: max(d.values())

# 32. Find the minimum value in a dictionary
min_dict_value = lambda d: min(d.values())

# 33. Check if a string contains only digits
contains_only_digits = lambda s: s.isdigit()

# 34. Check if a string contains only alphabets
contains_only_alpha = lambda s: s.isalpha()

# 35. Check if a string contains only alphanumeric characters
contains_only_alnum = lambda s: s.isalnum()

# 36. Check if a string contains only whitespace characters
contains_only_whitespace = lambda s: s.isspace()

# 37. Find the square root of a number
square_root = lambda x: x**0.5

# 38. Find the absolute value of a number
absolute_value = lambda x: abs(x)

# 39. Convert a list of strings to integers
strings_to_integers = lambda lst: list(map(int, lst))

# 40. Convert a list of strings to floats
strings_to_floats = lambda lst: list(map(float, lst))

# 41. Sort a list of tuples by the second element
sort_by_second = lambda lst: sorted(lst, key=lambda x: x[1])

# 42. Sort a dictionary by values
sort_dict_by_values = lambda d: {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

# 43. Merge two dictionaries
merge_dicts = lambda d1, d2: {**d1, **d2}

# 44. Count the occurrences of each element in a list
count_occurrences = lambda lst: {x: lst.count(x) for x in lst}

# 45. Check if two strings are anagrams
are_anagrams = lambda s1, s2: sorted(s1) == sorted(s2)

# 46. Check if a number is a power of 2
is_power_of_two = lambda n: n != 0 and (n & (n - 1)) == 0

# 47. Check if a number is a perfect square
is_perfect_square = lambda n: n > 0 and int(n**0.5)**2 == n

# 48. Merge two sorted lists into one sorted list
merge_sorted_lists = lambda lst1, lst2: sorted(lst1 + lst2)

# 49. Check if a list is empty
is_empty_list = lambda lst: not bool(lst)

# 50. Check if a string is empty
is_empty_string = lambda s: not bool(s)

# 51. Check if a list contains any duplicates
contains_duplicates = lambda lst: len(lst) != len(set(lst))

# 52. Convert a list of integers to binary strings
integers_to_binary = lambda lst: [bin(num) for num in lst]

# 53. Convert a binary string to an integer
binary_to_integer = lambda s: int(s, 2)

# 54. Convert a list of integers to hexadecimal strings
integers_to_hexadecimal = lambda lst: [hex(num) for num in lst]

# 55. Convert a hexadecimal string to an integer
hexadecimal_to_integer = lambda s: int(s, 16)

# 56. Swap the case of a string
swap_case = lambda s: s.swapcase()

# 57. Find the median of a list
median = lambda lst: sorted(lst)[len(lst)//2] if len(lst) % 2 != 0 else (sorted(lst)[len(lst)//2 - 1] + sorted(lst)[len(lst)//2]) / 2

# 58. Find the mode of a list
mode = lambda lst: max(set(lst), key=lst.count)

# 59. Check if a list is a subset of another list
is_subset = lambda lst1, lst2: set(lst1).issubset(set(lst2))

# 60. Check if a list is a superset of another list
is_superset = lambda lst1, lst2: set(lst1).issuperset(set(lst2))

# 61. Find the intersection of two lists
intersection = lambda lst1, lst2: list(set(lst1) & set(lst2))

# 62. Find the union of two lists
union = lambda lst1, lst2: list(set(lst1) | set(lst2))

# 63. Remove whitespace from both ends of a string
strip_whitespace = lambda s: s.strip()

# 64. Replace all occurrences of a substring in a string
replace_substring = lambda s, old, new: s.replace(old, new)

# 65. Convert a list of tuples to a dictionary
tuples_to_dict = lambda lst: {k: v for k, v in lst}

# 66. Check if a string is a valid email address
is_valid_email = lambda s: bool(re.match(r'^[\w\.-]+@[\w\.-]+$', s))

# 67. Check if a string contains any special characters
contains_special_characters = lambda s: not s.isalnum()

# 68. Find the longest word in a string
longest_word = lambda s: max(s.split(), key=len)

# 69. Find the shortest word in a string
shortest_word = lambda s: min(s.split(), key=len)

# 70. Check if a number is within a specified range
is_within_range = lambda num, lower, upper: lower <= num <= upper

# 71. Convert a list of tuples to a list of lists
tuples_to_lists = lambda lst: [list(t) for t in lst]

# 72. Check if a list is homogeneous (contains only one type of elements)
is_homogeneous = lambda lst: len(set(map(type, lst))) == 1

# 73. Convert a list of integers to Roman numerals
integers_to_roman = lambda num: ''.join(['I' * (num // 1),
                                         'IV' * (num // 4),
                                         'V' * (num // 5),
                                         'IX' * (num // 9),
                                         'X' * (num // 10),
                                         'XL' * (num // 40),
                                         'L' * (num // 50),
                                         'XC' * (num // 90),
                                         'C' * (num // 100),
                                         'CD' * (num // 400),
                                         'D' * (num // 500),
                                         'CM' * (num // 900),
                                         'M' * (num // 1000)])

# 74. Convert a Roman numeral to an integer
roman_to_integer = lambda s: sum([
    1 if c == 'I' else
    4 if c == 'IV' else
    5 if c == 'V' else
    9 if c == 'IX' else
    10 if c == 'X' else
    40 if c == 'XL' else
    50 if c == 'L' else
    90 if c == 'XC' else
    100 if c == 'C' else
    400 if c == 'CD' else
    500 if c == 'D' else
    900 if c == 'CM' else
    1000
    for c in [s[i:i+2] if s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM'] else s[i] for i in range(len(s))]])

# 75. Rotate a list to the right by n places
rotate_list_right = lambda lst, n: lst[-n:] + lst[:-n]

# 76. Rotate a list to the left by n places
rotate_list_left = lambda lst, n: lst[n:] + lst[:n]

# 77. Check if a string contains only ASCII characters
contains_only_ascii = lambda s: all(ord(char) < 128 for char in s)

# 78. Count the number of words in a string
count_words = lambda s: len(s.split())

# 79. Check if a number is a narcissistic number
is_narcissistic = lambda n: n == sum(int(digit)**len(str(n)) for digit in str(n))

# 80. Find the sum of all even numbers in a list
sum_of_evens = lambda lst: sum(num for num in lst if num % 2 == 0)

# 81. Find the sum of all odd numbers in a list
sum_of_odds = lambda lst: sum(num for num in lst if num % 2 != 0)

# 82. Check if a number is a perfect number
is_perfect_number = lambda n: n == sum(i for i in range(1, n) if n % i == 0)

# 83. Check if a string contains only printable characters
contains_only_printable = lambda s: all(char.isprintable() for char in s)

# 84. Check if a number is a palindrome
is_number_palindrome = lambda n: str(n) == str(n)[::-1]

# 85. Count the number of words starting with a specific letter in a string
count_words_starting_with = lambda s, letter: sum(1 for word in s.split() if word.startswith(letter))

# 86. Find the ASCII value of a character
ascii_value = lambda char: ord(char)

# 87. Find the character corresponding to an ASCII value
ascii_to_char = lambda value: chr(value)

# 88. Find the number of occurrences of a substring in a string
count_substring_occurrences = lambda s, sub: s.count(sub)

# 89. Calculate the average of a list of numbers
average = lambda lst: sum(lst) / len(lst) if lst else 0

# 90. Check if a number is a happy number
is_happy_number = lambda n: n == 1 or n == 7 or is_happy_number(sum(int(d)**2 for d in str(n)))

# 91. Check if a string is a pangram
is_pangram = lambda s: set(string.ascii_lowercase) <= set(s.lower())

# 92. Find the first non-repeating character in a string
first_non_repeating_character = lambda s: next((char for char in s if s.count(char) == 1), None)

# 93. Find the ASCII difference between two characters
ascii_difference = lambda char1, char2: abs(ord(char1) - ord(char2))

# 94. Find the second largest number in a list
second_largest = lambda lst: sorted(set(lst))[-2]

# 95. Find the second smallest number in a list
second_smallest = lambda lst: sorted(set(lst))[1]

# 96. Check if a number is a harshad number
is_harshad_number = lambda n: n % sum(int(digit) for digit in str(n)) == 0

# 97. Check if a number is a strong number
is_strong_number = lambda n: n == sum(math.factorial(int(digit)) for digit in str(n))

# 98. Convert a list of integers to a list of strings
integers_to_strings = lambda lst: list(map(str, lst))

# 99. Convert a list of strings to title case
to_title_case = lambda lst: [word.title() for word in lst]

# 100. Calculate the sum of ASCII values of all characters in a string
sum_of_ascii_values = lambda s: sum(ord(char) for char in s)