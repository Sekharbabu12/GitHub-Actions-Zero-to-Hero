# greeting.py
def get_name():
    return input("Somasekhar")

name = get_name()


# greeting.py
def get_name(input_func=input):
    return input_func("Enter your name: ")

if __name__ == "__main__":
    name = get_name()
    print(f"Hello, {name}!")



