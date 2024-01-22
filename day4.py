# String methods in Python

# capitalize() - Converts the first character of a string to uppercase
string = "hello world"
capitalized_string = string.capitalize()
print(capitalized_string)  # Output: Hello world

# lower() - Converts all characters in a string to lowercase
string = "HELLO WORLD"
lowercase_string = string.lower()
print(lowercase_string)  # Output: hello world

# upper() - Converts all characters in a string to uppercase
string = "hello world"
uppercase_string = string.upper()
print(uppercase_string)  # Output: HELLO WORLD

# swapcase() - Swaps the case of all characters in a string
string = "Hello World"
swapped_case_string = string.swapcase()
print(swapped_case_string)  # Output: hELLO wORLD

# title() - Converts the first character of each word in a string to uppercase
string = "hello world"
title_string = string.title()
print(title_string)  # Output: Hello World

# strip() - Removes leading and trailing whitespace from a string
string = "   hello world   "
stripped_string = string.strip()
print(stripped_string)  # Output: hello world

# split() - Splits a string into a list of substrings based on a delimiter
string = "hello,world"
split_string = string.split(",")
print(split_string)  # Output: ['hello', 'world']

# join() - Joins a list of strings into a single string using a specified delimiter
list_of_strings = ['hello', 'world']
joined_string = ",".join(list_of_strings)
print(joined_string)  # Output: hello,world

# replace() - Replaces all occurrences of a substring in a string with another substring
string = "hello world"
replaced_string = string.replace("world", "universe")
print(replaced_string)  # Output: hello universe

# find() - Returns the index of the first occurrence of a substring in a string
string = "hello world"
index = string.find("world")
print(index)  # Output: 6

# count() - Returns the number of occurrences of a substring in a string
string = "hello world"
count = string.count("o")
print(count)  # Output: 2

# len() - Returns the length of a string
string = "hello world"
length = len(string)
print(length)  # Output: 11

print(string[2:8])








