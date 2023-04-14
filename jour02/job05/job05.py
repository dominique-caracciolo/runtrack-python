def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        return num1 / num2
    elif operator == "*":
        return num1 * num2
    elif operator == "%":
        return num1 % num2
    else:
        print("wrong entry")

print(calcule(10 ,"+", 22))
print(calcule(10 ,"*", 22))
print(calcule(10 ,"/", 22))
print(calcule(10 ,"-", 22))
print(calcule(10 ,"%", 22))




