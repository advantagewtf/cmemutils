from imports import *
def rand_string(length=16) -> str:
    """
    Generate a random string of specified length using ASCII letters.

    Args:
        length (int): The length of the random string to generate. Defaults to 16.

    Returns:
        str: A randomly generated string of the specified length.
    """
    rand_str = ""
    for i in range(length):
        rand_str += random.choice(string.ascii_letters)
    return rand_str

def randint(low: int, high: int) -> int:
    return random.randint(low, high)
