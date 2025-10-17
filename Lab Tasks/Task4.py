class basic_calc:
    """
    A basic calculator class that performs arithmetic operations on two integers
    """
    
    def __init__(self, num1, num2):
        """
        Constructor to initialize the two numbers
        
        Args:
            num1 (int): First number
            num2 (int): Second number
        """
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        """
        Method to add the two numbers
        
        Returns:
            int: Sum of num1 and num2
        """
        return self.num1 + self.num2
    
    def subtraction(self):
        """
        Method to subtract the two numbers (num1 - num2)
        
        Returns:
            int: Difference between num1 and num2
        """
        return self.num1 - self.num2
    
    def multiplication(self):
        """
        Method to multiply the two numbers
        
        Returns:
            int: Product of num1 and num2
        """
        return self.num1 * self.num2
    
    def division(self):
        """
        Method to divide the two numbers (num1 / num2)
        
        Returns:
            float: Result of division
            str: Error message if division by zero
        """
        if self.num2 == 0:
            return "Error: Division by zero is not allowed!"
        return self.num1 / self.num2
    
    def display_numbers(self):
        """
        Method to display the current numbers
        """
        print(f"Current numbers: {self.num1} and {self.num2}")
    
    def update_numbers(self, new_num1, new_num2):
        """
        Method to update the numbers
        
        Args:
            new_num1 (int): New first number
            new_num2 (int): New second number
        """
        self.num1 = new_num1
        self.num2 = new_num2
        print(f"Numbers updated to: {self.num1} and {self.num2}")

def main():
    """
    Main function to demonstrate the basic_calc class
    """
    print("=== BASIC CALCULATOR DEMONSTRATION ===")
    print()
    
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        calc = basic_calc(num1, num2)
        
        calc.display_numbers()
        print("-" * 40)
        
        print(f"Addition: {calc.num1} + {calc.num2} = {calc.addition()}")
        print(f"Subtraction: {calc.num1} - {calc.num2} = {calc.subtraction()}")
        print(f"Multiplication: {calc.num1} × {calc.num2} = {calc.multiplication()}")
        print(f"Division: {calc.num1} ÷ {calc.num2} = {calc.division()}")
        
        print("-" * 40)
        
        print("\nLet's update the numbers and perform operations again:")
        new_num1 = int(input("Enter new first number: "))
        new_num2 = int(input("Enter new second number: "))
        
        calc.update_numbers(new_num1, new_num2)
        print("-" * 40)
        
        print(f"Addition: {calc.num1} + {calc.num2} = {calc.addition()}")
        print(f"Subtraction: {calc.num1} - {calc.num2} = {calc.subtraction()}")
        print(f"Multiplication: {calc.num1} × {calc.num2} = {calc.multiplication()}")
        print(f"Division: {calc.num1} ÷ {calc.num2} = {calc.division()}")
        
    except ValueError:
        print("Error: Please enter valid integers!")
    except Exception as e:
        print(f"An error occurred: {e}")

def simple_demo():
    """
    Simple demonstration without user input
    """
    print("=== SIMPLE DEMONSTRATION ===")
    
    calc1 = basic_calc(10, 5)
    calc2 = basic_calc(8, 2)
    calc3 = basic_calc(15, 0)
    
    print("Calculator 1 (10, 5):")
    print(f"Addition: {calc1.addition()}")
    print(f"Subtraction: {calc1.subtraction()}")
    print(f"Multiplication: {calc1.multiplication()}")
    print(f"Division: {calc1.division()}")
    print()
    
    print("Calculator 2 (8, 2):")
    print(f"Addition: {calc2.addition()}")
    print(f"Subtraction: {calc2.subtraction()}")
    print(f"Multiplication: {calc2.multiplication()}")
    print(f"Division: {calc2.division()}")
    print()
    
    print("Calculator 3 (15, 0) - Testing division by zero:")
    print(f"Addition: {calc3.addition()}")
    print(f"Subtraction: {calc3.subtraction()}")
    print(f"Multiplication: {calc3.multiplication()}")
    print(f"Division: {calc3.division()}")

if __name__ == "__main__":
    
    main()
    
    print("\n" + "="*50 + "\n")
    
    simple_demo()