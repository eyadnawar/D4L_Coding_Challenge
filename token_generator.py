import string
import random

def generate_tokens(file_path, numOfChars):
    file_path = file_path
    numOfChars = numOfChars

    file = open(file_path, 'w')

    for i in range (0, int(1e7)):
        file.write("".join(random.choices(string.ascii_lowercase, k = numOfChars)) + '\n')

    file.close()
    return
