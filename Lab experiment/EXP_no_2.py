def list_operations():
    l = []
    try:
        # Add elements to the list
        for _ in range(int(input("How many elements to add?: "))):
            l.append(int(input("Enter an element: ")))

        # Append an element
        l.append(int(input("Enter an element to append: ")))

        # Insert an element at a specific position
        pos = int(input("Enter position to insert an element: "))
        ele = int(input("Enter the element to insert: "))
        if 0 <= pos <= len(l):
            l.insert(pos, ele)
        else:
            print("Invalid position!")

        # Remove an element by value
        val = int(input("Enter the element to remove: "))
        if val in l:
            l.remove(val)
        else:
            print("Element not found!")

        # Print the final list
        print("Final list:", l)

    except ValueError:
        print("Invalid input! Please enter numbers only.")


def tuple_operations():
    t = (10, 20, 'Sita', 30, 40, 'Ram')
    print(f"First element: {t[0]}")
    print(f"Last element: {t[-1]}")
    print(f"First three elements: {t[:3]}")


def menu():
    while True:
        print("\n==== Main Menu ====")
        print("1. List Operations")
        print("2. Tuple Operations")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                list_operations()
            elif choice == 2:
                tuple_operations()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")


menu()