"""
Create a program that implements a stack using a list. Add a method, safe_pop(), which safely removes the top element from the stack. If the stack is empty, the method should handle this condition by:
2.1) Printing a message as ""Stack is empty, nothing to pop.""
2.2) Returning None
"""

class Stack:
    def __init__(self):
        self.stack = []

    # Push element onto stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack.")

    # Safe pop method
    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()

    # Display stack
    def display(self):
        print("Stack:", self.stack)


s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop (safe_pop)")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = input("Enter value to push: ")
        s.push(val)

    elif choice == 2:
        result = s.safe_pop()
        if result is not None:
            print(f"Popped element: {result}")

    elif choice == 3:
        s.display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")