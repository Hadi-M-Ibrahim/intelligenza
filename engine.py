import sys

def load_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            file_contents = file.read()
        return file_contents
    except Exception as err:
        print(f"Error loading file '{file_name}' insure the file exists in the current directory. Also be sure to incldude the .py file extension: {err}")
        sys.exit(1)

