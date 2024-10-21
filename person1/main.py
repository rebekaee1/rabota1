# main.py
from file_reader import read_file
from file_writer import write_file

if __name__ == "__main__":
    filename = "example.txt"
    content = read_file(filename)
    print(f"File content: {content}")
    new_content = input("Enter new content to write: ")
    write_file(filename, new_content)
    print("This is a new update in person1")
