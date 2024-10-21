import random
import string


def generate_random_string(length=7):
    # Define the character set (excluding characters that might cause issues in URLs)
    characters = string.ascii_letters + string.digits + "-_"

    # Generate the random string
    random_string = "".join(random.choice(characters) for _ in range(length))

    # Ensure the string doesn't start or end with a dash or underscore
    while random_string[0] in "-_" or random_string[-1] in "-_":
        random_string = "".join(random.choice(characters) for _ in range(length))

    return random_string
