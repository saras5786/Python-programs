class Converter:
    
    # Method to convert inches to feet
    def toFeet(self, inches):
        return inches / 12.0


# Main execution
inches = int(input())

obj = Converter()
feet = obj.toFeet(inches)

print(feet)
