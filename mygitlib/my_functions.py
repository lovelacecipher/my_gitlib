import time
import pyfiglet
from colorama import Fore, Style

# For print_banner
def print_banner(text):
  banner = pyfiglet.figlet_format(text, font="ansi_shadow")
  print(Fore.CYAN + Style.BRIGHT + banner + Style.RESET_ALL)

#Loading Splash Screen
def splash_screen():
  print_banner("My GitLab")
  print(Fore.MAGENTA + Style.BRIGHT + "Welcome to My GitLib - Your Python Utility Toolkit" + Style.RESET_ALL)
  print(Fore.YELLOW + "Loading..." + Style.RESET_ALL)
  input()

# Say Hello
def say_hello(name):
  return f"Hello, {name}! Welcome to my gitlib"

# Add two numbers
def add_numbers(a, b):
  return a + b

# make text uppercase
def make_uppercase(text):
  return text.upper()

#save text to file
def save_to_file(filename, text):
  with open(filename, 'w') as f:
    f.write(text)
  return f"saved to {filename}"
