RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def yellow(text):
    return f"{YELLOW}{text}{RESET}"
def red(text):
    return f"{RED}{text}{RESET}"
def green(text):
    return f"{GREEN}{text}{RESET}"