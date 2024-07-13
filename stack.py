class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)        
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements are:", self.stack)
def main():
    stack = Stack()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if stack is empty")
        print("5. Display stack")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == 2:
            popped_item = stack.pop()
            print(f"Popped item: {popped_item}")
        elif choice == 3:
            top_item = stack.peek()
            print(f"Top item: {top_item}")
        elif choice == 4:
            if stack.is_empty():
                print("Stack is empty")
            else:
                print("Stack is not empty")
        elif choice == 5:
            stack.display()
        elif choice == 6:
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
