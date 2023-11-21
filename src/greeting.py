
# greeting.py
def get_name(input_func=input):
    return input_func("Somasekhar")

if __name__ == "__main__":
    name = get_name()
    print(f"Hello, {name}!")


# test_greeting.py
from unittest.mock import patch
from greeting import get_name

def test_get_name():
    with patch('builtins.input', return_value='Somasekhar'):
        assert get_name() == 'Somasekhar'

