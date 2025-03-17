class Calculator:
    
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
calculator = Calculator()
    
x = float(input("Enter 1st number:"))
y = float(input("Enter 2nd number:"))
    
add_result = calculator.add(x, y)
sub_result = calculator.subtract(x, y)
    
print("Sum is: ", add_result)
print("Difference is: ", sub_result)
