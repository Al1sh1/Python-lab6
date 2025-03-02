from functools import reduce
import os
import math
import time
import shutil
# Python builtin functions exercises
# Task 1: Multiply all numbers in a list
def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

# Task 2: Count uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Task 3: Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Task 4: Invoke square root function after specific milliseconds
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

# Task 5: Check if all elements in a tuple are True
def all_true(tpl):
    return all(tpl)

# Python Directories and Files exercises
# Task 6: List only directories, files, and all items in a specified path
def list_files_dirs(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return files, dirs

# Task 7: Check access to a specified path (existence, readability, writability, executability)
def check_path_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

# Task 8: Test if a path exists and find filename and directory portion
def path_info(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    return None

# Task 9: Count the number of lines in a text file
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

# Task 10: Write a list to a file
def write_list_to_file(filename, lst):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")

# Task 11: Generate 26 text files named A.txt to Z.txt
def generate_text_files():
    for char in range(65, 91):  # ASCII codes for A-Z
        with open(f"{chr(char)}.txt", 'w') as f:
            f.write(f"This is {chr(char)}.txt file\n")

# Task 12: Copy the contents of one file to another
def copy_file(src, dest):
    shutil.copy(src, dest)

# Task 13: Delete a file by specified path after checking access and existence
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False

print(multiply_list([1, 2, 3, 4]))
print(count_case("Hello World!"))
print(is_palindrome("madam"))
print(is_palindrome("eshak"))
print(f"Square root: {delayed_sqrt(25100, 2123)}")
print(all_true((True, True, False)))
print(list_files_dirs("."))
print(check_path_access("./test.txt"))
print(path_info("./test.txt"))
write_list_to_file("output.txt", ["apple", "banana", "cherry"])
generate_text_files()

