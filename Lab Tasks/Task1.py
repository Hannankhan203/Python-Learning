print("1. Soup and salad")
print("2. Pasta with meat sauce")
print("3. Chef's special")
print()

choice = input("Which number would you like to order? ")

if choice == "1":
    print("One Soup and salad coming right up!")
elif choice == "2":
    print("One Pasta with meat sauce coming right up!")
elif choice == "3":
    print("One Chef's special coming right up!")
else:
    print("Sorry, that is not a valid choice.")