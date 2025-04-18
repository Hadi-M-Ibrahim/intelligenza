import sys

def load_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            file_contents = file.read()
        return file_contents
    except Exception as err:
        print(f"Error loading file '{file_name}' insure the file exists in the current directory. Also be sure to incldude the .py file extension: {err}")
        sys.exit(1)

def opt_instruction(args):
    if args.o0:
        return "Convert the following Python code to x86-64 assembly (GAS, AT&T syntax) with a direct, line-by-line translation. Do not apply any optimizations. Return only the assembly code and nothing else. Python code: "
    if args.o1:
        return "Convert the following Python code to x86-64 assembly (GAS, AT&T syntax), applying only standard compiler optimizations (such as those performed at -O2 level). Return only the assembly code and nothing else. Python code: "
    return "Convert the following Python code to x86-64 assembly (GAS, AT&T syntax), making aggressive optimizations, including algorithmic (Big O) improvements where possible. Return only the assembly code and nothing else. Python code: "
