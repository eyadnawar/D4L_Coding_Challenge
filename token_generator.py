import string
import random

def generate_tokens(file_path, numOfChars):
    file_path = file_path
    numOfChars = numOfChars
    
    try:
        file = open(file_path, 'w')
        
    except:
        print("error, could not create file.")

    for i in range (0, int(1e7)):
        file.write("".join(random.choices(string.ascii_lowercase, k = numOfChars)) + '\n')

    file.close()
    return
