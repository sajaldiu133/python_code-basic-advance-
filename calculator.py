a = float(input('Enter number 1 = '))
b = float(input('Enter number 2 = '))
operator = input("Choose operator (+ - / * %) = ")

if operator == "+":
    result = a + b
    print("SUM =", result)
    
elif operator == "-":
    result = a - b
    print("SUB =", result)  

elif operator == "*":
    result = a * b
    print("MULTI =", result) 

elif operator == "/":
    if b != 0:
        print("DIV =", a / b)
    else:
        print("Undefined: Division by zero")
        
elif operator == "%":
    if b != 0:
        print("MOD =", a % b)
    else:
        print("Undefined: Modulo by zero")
        
else:
    print("Invalid operator")
