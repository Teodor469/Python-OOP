def even_numbers(function): 
    def wrapper(numbers): 
        result = [num for num in numbers if num % 2 == 0]
        return result
    return wrapper