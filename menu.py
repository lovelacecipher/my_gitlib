from mygitlib import say_hello, add_numbers, make_uppercase, save_to_file
from mygitlib.my_functions import splash_screen, print_banner
from colorama import Fore, Style, init
import os
import pyfiglet
import time


init(autoreset=True)


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


def menu():
  while True:
    clear_screen()

    # Banner
    banner = pyfiglet.figlet_format("My GitLib", font="ansi_shadow")
    print(Fore.CYAN + Style.BRIGHT + banner + Style.RESET_ALL)
    print(Fore.MAGENTA + "-" * 50 + Style.RESET_ALL)
    
    # Menu Options
    print(Fore.CYAN + Style.BRIGHT + "=== My GitLib Interactive Menu ===" + Style.RESET_ALL)
    print(Fore.YELLOW + "1." + Style.RESET_ALL + "Say Hello")
    print(Fore.YELLOW + "2." + Style.RESET_ALL + "Add 2 Numbers")
    print(Fore.YELLOW + "3." + Style.RESET_ALL + "Make Text Uppercase")
    print(Fore.YELLOW + "4." + Style.RESET_ALL + "Save Text to a File")
    print(Fore.RED + "5." + Style.RESET_ALL + "Exit\n")

    choice = input(Fore.GREEN + "Choose an option (1-5): " + Style.RESET_ALL)

    if choice == "1":
      name = input("Enter your name: ")
      print(Fore.CYAN + say_hello(name))
      input(Fore.MAGENTA + "\nPress Enter to Continue...")

    elif choice == "2":
      a = float(input("Enter first number: "))
      b = float(input("Enter second number: "))
      print(Fore.CYAN + f"Result: {add_numbers(a, b)}")
      input(Fore.MAGENTA + "\nPress Enter to Continue...")

    elif choice == "3":
      text = input("Enter Text:")
      print(Fore.CYAN + f"Uppercase: {make_uppercase(text)}")
      input(Fore.MAGENTA + "\nPress Enter to Continue...")

    elif choice == "4":
      filename = input("Enter filename (e.g., output.txt): ")
      text = input("Enter text to save: ")
      print(Fore.CYAN + save_to_file(filename, text))
      input(Fore.MAGENTA + "\nPress Enter to Continue...")

    elif choice == "5":
      print(Fore.RED + "goodbye")
      break

    else:
      print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
  splash_screen()
  menu()