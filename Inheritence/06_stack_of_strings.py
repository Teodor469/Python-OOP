class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str) -> None:
        """Adds an element at the end of the stack."""
        self.data.append(element)

    def pop(self) -> str:
        """Removes and returns the last element in the stack."""
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def top(self) -> str:
        """Returns a reference to the topmost element of the stack."""
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("Stack is empty. No top element available.")

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, otherwise False."""
        return len(self.data) == 0

    def __str__(self) -> str:
        """Override the string method to return stack data in the specified format."""
        elements = [f"{element}" for element in reversed(self.data)]
        return "[" + ", ".join(elements) + "]"