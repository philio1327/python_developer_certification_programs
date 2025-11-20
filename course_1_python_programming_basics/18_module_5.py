## Exception handling assignment
def read_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            print("File successfully opened!")

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")