"""Demonstrates Basic List Syntax"""

# Create empty list
grocery_list: list[str] = list() # <- constructor
grocery_list: list[str] = [ ] # <- literal, same as above
print("Empty list")
print(grocery_list)

# Add to list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things:")
print(grocery_list)

# Create list with objects in it
gorcery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list:")
print(grocery_list)
print("Add another thing: ")
gorcery_list2.append("whipped cream")
print(gorcery_list2)

# Indexing
print("Printing one item")
print(grocery_list[2])

# Modifying by Index
grocery_list[0] = "Cinnamon Toast Crunch"
print("Modifying")
print(grocery_list)

#Length of a list:
print("length")
print(len(grocery_list))

# Remove an item from list
grocery_list.pop(1)
print("remove an item")
print(grocery_list)


# Function name: display
# Parameter: list[str]
# return nothing
# Print out the list
# Print ~*~ Functions~*~

def display(my_list: list[str]):
    print(my_list)

display(grocery_list)
x = display(["Anusha", "Jack", "Virinda"])
print(x)


# Create a list
# Name: create
# Parameters: str and str
# RV: list[str]
# Put both parameters into list and return that list

def create(word1: str, word2: str) -> list[str]:
    new_list: list[str] = [word1, word2]
    return new_list

x: list[str] = create("Hello","Hello")
print(x)
    

