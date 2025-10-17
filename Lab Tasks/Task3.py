def get_numbers(count):
    """
    Function to get numbers from the user
    
    Args:
        count (int): Number of values to get from user
    
    Returns:
        list: List of numbers entered by user
    """
    numbers = []
    print(f"Please enter {count} numbers:")
    
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    return numbers

def find_largest(numbers):
    """
    Function to find the largest number in a list
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        float: The largest number in the list
    """
    if not numbers:
        return None
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

def display_result(numbers, largest):
    """
    Function to display the result
    
    Args:
        numbers (list): List of numbers entered by user
        largest (float): The largest number found
    """
    print("\n" + "="*40)
    print("RESULTS")
    print("="*40)
    print(f"Numbers entered: {numbers}")
    print(f"Largest number: {largest}")
    print("="*40)

def main():
    """
    Main function to coordinate the program flow
    """
    print("LARGEST NUMBER FINDER")
    print("="*40)
    
    numbers = get_numbers(10)
    
    largest = find_largest(numbers)
    
    display_result(numbers, largest)

if __name__ == "__main__":
    main()