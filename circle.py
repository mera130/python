def circle_calculator():
    

    PI = 3.14159
    
    print("Circle Area and Perimeter Calculator")
    print("-----------------------------------")
    
    try:
        
        radius = float(input("Enter the radius of the circle: "))
        
        if radius <= 0:
            print("mistake ditected: Radius must be a positive number.")
            return
        
        # calculating
        area = PI * radius ** 2
        perimeter = 2 * PI * radius
        
        # result
        print(f"\nResults for circle with radius {radius}:")
        print(f"Area: {area:.2f}")
        print(f"Perimeter: {perimeter:.2f}")
        
    except ValueError:
        print("Error: Please enter a valid number.")
        
if __name__ == "__main__":
    circle_calculator()
