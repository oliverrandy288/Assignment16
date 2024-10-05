class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        # Private attributes
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, name):
        self.__category_name = name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, budget):
        if budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget  # Reset remaining budget when allocated budget changes
        else:
            print("Budget must be a positive number.")

    # Method to add an expense
    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"Expense of {amount} added to {self.__category_name}. Remaining budget: {self.__remaining_budget}")
            else:
                print(f"Insufficient budget in {self.__category_name}. You only have {self.__remaining_budget} left.")
        else:
            print("Expense amount must be a positive number.")

    # Method to display category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")


# Testing the class

# Task 1: Create a budget category
food_category = BudgetCategory("Food", 500)

# Task 2: Use getters and setters
print(food_category.get_category_name())  # Output: Food
food_category.set_allocated_budget(600)   # Update the budget to 600
print(food_category.get_allocated_budget())  # Output: 600

# Task 3: Add expenses
food_category.add_expense(100)  # Deducts 100 from the food budget
food_category.add_expense(50)   # Deducts another 50 from the food budget

# Task 4: Display category summary
food_category.display_category_summary()  
