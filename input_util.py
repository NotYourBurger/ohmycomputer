import colors_util
def read_int(text, low, high):
    
    while True:
        try:
            usr_input = int(input(text))
            if low <= usr_input <= high:
                break
            print(colors_util.yellow(f"Please insert number between {low} - {high}"))
        except ValueError:
            print(colors_util.yellow(f"Please Enter a valid number between {low} - {high}"))
    return usr_input