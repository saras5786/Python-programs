try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)

except ZeroDivisionError:
    print("Error: Division by zero")

except ValueError:
    print("Error: Invalid input")

except Exception as e:
    print("Error:", e)
