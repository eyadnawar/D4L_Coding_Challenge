import string
import random
from token_reader_HashSet import token_reader_hashset
from token_reader_sorting import token_reader_sorted_tokens

def generate_tokens():
    file_path = 'C:/Users/Lenovo/Desktop/D4L.txt'
    s = 7
    random_string = "".join(random.choices(string.ascii_lowercase, k = s))

    file = open(file_path, 'w')

    for i in range (0, int(1e7)):
        file.write("".join(random.choices(string.ascii_lowercase, k = 7)) + '\n')

    file.close()
    return

if __name__ == "__main__":
    generate_tokens()
    token_reader_hashset()
    token_reader_sorted_tokens()
