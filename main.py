from token_reader_HashSet import token_reader_hashset
from token_reader_sorting import token_reader_sorted_tokens

if __name__ == "__main__":
  file_path = 'C:/Users/Lenovo/Desktop/D4L.txt'
  numOfChars = 7
  generate_tokens(file_path, numOfChars)
  token_reader_hashset(file_path)
  token_reader_sorted_tokens(file_path)
