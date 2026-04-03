"""
Write a program to demonstrate fundamental file handling operations including opening a file, reading its contents, writing data to it, appending additional content and ensuring proper closing of the file.
"""

# 1. Writing to a file (this will create the file if it doesn't exist)
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This file is created using Python.\n")
file.close()   # Closing the file

print("Data written successfully.\n")

# 2. Reading the file
file = open("sample.txt", "r")
content = file.read()
print("Reading file content:")
print(content)
file.close()   # Closing the file

# 3. Appending data to the file
file = open("sample.txt", "a")
file.write("This line is added later using append mode.\n")
file.close()   # Closing the file

print("\nData appended successfully.\n")

# 4. Reading again to see updated content
file = open("sample.txt", "r")
content = file.read()
print("Updated file content:")
print(content)
file.close()   # Closing the file