while True:
    print("\n**geometry helper** \n \n1. Triangle area calculator \n2. Squere area calculator \n3. Circle area calculator\n4. Pythagoras triad checker\n5. Calculator\n6. Exit")
    menu_input = int(input("enter your choose "))
    match menu_input:
        case 6:
            break
        case 1:
            Data_triangle = input("To calculate the area of a triangle, enter the base of the triangle and the height of the triangle. Enter the data with one space between them. ")
            Data_triangle = Data_triangle.split(" ")
            Data_triangle[0] = float(Data_triangle[0])
            Data_triangle[1] = float(Data_triangle[1])
            print(f"The area of the triangle is {Data_triangle[0] * Data_triangle[1] / 2}")
        case 2:
            Data_square = input("To calculate the area of a square, enter the base of the square and the height of the square. Enter the data with one space between them. ")
            Data_square = Data_square.split(" ")
            Data_square[0] = float(Data_square[0])
            Data_square[1] = float(Data_square[1])
            print(f"The area of the square is {Data_square[0] * Data_square[1]}")
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass