def reverse_text(string):
    current = len(string) - 1
    while current >= 0:
        yield string[current]
        current -= 1