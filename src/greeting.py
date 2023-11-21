# greeting.py
def get_name():
    return input("Somasekhar")

name = get_name()


# test_greeting.py
from greeting import get_name

def test_get_name():
    # You can use a testing library to mock user input
    # or directly provide the input depending on your needs
    assert get_name() == "Somasekhar"


