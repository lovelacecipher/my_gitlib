import json
import os
import pyfiglet
import matplotlib.pyplot as plt
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True) # Automatically resets colors after each print


DATA_FILE = "expenses.json"
CATEGORIES = ["Food", "Transport", "Entertainment", "Other"]


def clear_screen():
  """Clear terminal screen."""
  os.system('cls' if os.name == 'nt' else 'clear')


def pause():
  """Wait for user input."""
  input(Fore.YELLOW + "\nPress enter to continue...")


def load_expenses():
  """Load Expenses from the JSON file."""
  if not os.path.exists(DATA_FILE):
    return[]   # If the file doesn't exist returns an empty list
  with open(DATA_FILE, "r") as file:
    return json.load(file)
  

def save_expenses(expenses):
  """Save expenses to the JSON file."""
  with open(DATA_FILE, "w") as file:
    json.dump(expenses, file, indent=4)


def add_expense():
  """Add a new expense with validation."""
  try:
    date = input("Enter date (YYYY-MM-DD): ").strip()
    datetime.strptime(date, "%Y-%m-%d") # Validate date format
    while True:
      print(Fore.YELLOW + f"Available categories {', '.join(CATEGORIES)}")
      category = input("Enter category: ").strip().title()
      if category in CATEGORIES:
        break
      else:
        print(Fore.RED + f"Invalid category! Please choose from: {', '.join(CATEGORIES)}.\n")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ").strip()

    expense = {
      "date": date,
      "category": category,
      "amount": amount,
      "description": description
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print(Fore.GREEN + Style.BRIGHT + "Expense added successfully!\n")

  except ValueError:
    print(Fore.RED + Style.BRIGHT + "Invalid input! Please check your date and amount.\n")


def view_expenses():
  """Display all recorded expenses."""
  expenses = load_expenses()
  if not expenses:
    print(Fore.YELLOW + "No expenses recorded yet.\n")
    return
  print(Fore.BLUE + Style.BRIGHT + "\n--- All Expenses ---")
  for idx, e in enumerate(expenses, 1):
    print(f"{Fore.CYAN}{idx}. {e['date']} | {e['category']} | {e['amount']:.2f} | {e['description']}")
  print()


def view_total():
  """Display the total amount spent."""
  expenses = load_expenses()
  total = sum(e["amount"] for e in expenses)
  print(Fore.GREEN + Style.BRIGHT + f"\nTotal Spent: ${total:.2f}\n")


def filter_expenses():
  """Filter expenses by category."""
  while True:
    print(Fore.YELLOW + f"Available categories: {', '.join(CATEGORIES)}")
    category = input(Fore.CYAN + "Enter category to filer: ").strip().title()
    if category in CATEGORIES:
      break
    else:
      print(Fore.RED + f"Invalid Category! Please choose from: {', '.join(CATEGORIES)}.\n")


  expenses = load_expenses()
  filtered = [e for e in expenses if e["category"] == category]
  if not filtered:
    print(Fore.YELLOW + f"No expenses found for category: {category}\n")
    return
  print(Fore.BLUE + Style.BRIGHT + f"\n--- Expenses in {category} ---")
  for idx, e in enumerate(filtered, 1):
    print(f"{Fore.CYAN}{idx}. {e['date']} | ${e['amount']:.2f} | {e['description']}")
  print()


def manage_categories():
  """Manage categories (add/remove)."""
  while True:
    clear_screen()
    print(Fore.BLUE + Style.BRIGHT + "\n--- Manage Categories ---")
    print(Fore.YELLOW + f"Current categories: {', '.join(CATEGORIES)}")
    print("1. Add Category")
    print("2. Remove Category")
    print("3. Back to Main Menu\n")
    choice = input(Fore.MAGENTA + "Choose an option: ").strip()

    if choice == "1":
      new_cat = input("Enter new category name: ").strip().title()
      if new_cat in  CATEGORIES:
        print(Fore.RED + "Category already exists!\n")
      elif new_cat:
        CATEGORIES.append(new_cat)
        print(Fore.GREEN + f"Category '{new_cat}' added.\n")
      else:
        print(Fore.RED + "Category name cannot be empty!\n")
      pause()
    elif choice == "2":
      rem_cat = input("Enter category to remove: ").strip().title()
      if rem_cat in CATEGORIES:
        CATEGORIES.remove(rem_cat)
        print(Fore.GREEN + f"Category '{rem_cat}' removed.\n")
      else:
        print(Fore.RED + "Category not found!\n")
      pause()
    elif choice == "3":
      break
    else:
      print(Fore.RED + "Invalid choice. Try again.\n")


def view_spending_chart():
    """Display a bar chart of spending by category."""
    expenses = load_expenses()
    if not expenses:
        print(Fore.YELLOW + "No expenses to display.\n")
        return

    # Sum amounts by category
    category_totals = {}
    for e in expenses:
        category_totals[e['category']] = category_totals.get(e['category'], 0) + e['amount']

    chart_categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Plot bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(chart_categories, amounts)
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent ($)")
    plt.tight_layout()
    plt.show()


def main_menu():
  """Main CLI loop."""
  while True:
    # Fancy header with background + bold text
    clear_screen()
    banner = pyfiglet.figlet_format("Expense Tracker", font="ansi_shadow")
    print(Fore.WHITE + Style.BRIGHT + banner)
    
    print(Fore.CYAN + "1. Add Expense")
    
    print("2. View All Expenses")
    
    print("3. View Total Spent")
    
    print("4. View Spending Chart")

    print("5. Filter by Category")
    
    print("6. Manage Categories")

    print("7. Exit")
    
    choice = input(Fore.MAGENTA + Style.BRIGHT + "Choose an Option: ").strip()

    if choice == "1":
      add_expense()
      pause()
    elif choice == "2":
      view_expenses()
      pause()
    elif choice == "3":
      view_total()
      pause()
    elif choice == "4":
      view_spending_chart()
      pause()
    elif choice == "5":
      filter_expenses()
      pause()
    elif choice == "6":
      manage_categories()
      pause()
    elif choice == "7":
      print(Fore.GREEN + Style.BRIGHT + "Goodbye!")
      break
    else:
      print(Fore.RED + Style.BRIGHT + "Invalid option, please try again.\n")



if __name__ == "__main__":
  main_menu()