
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile opened successfully!")
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You do not have permission to read this file.")

except Exception as e:
    print("An unexpected error occurred:", e)