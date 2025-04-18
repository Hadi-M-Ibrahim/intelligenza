import sys
from openai import OpenAI
import os

def load_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            file_contents = file.read()
        return file_contents
    
    except Exception as err:
        print(f"Error loading file '{file_name}' insure the file exists in the current directory. Also be sure to include the .py file extension: {err}")
        sys.exit(1)

def opt_instruction(args):
    if args.o0:
        return "Convert the following Python code to x86-64 assembly (GAS, AT&T syntax) with a direct, line-by-line translation. Do not apply any optimizations. Return only the assembly code and nothing else. Python code: "
    if args.o1:
        return "Convert the following Python code to x86-64 assembly (GAS, AT&T syntax), applying only standard compiler optimizations (such as those performed at -O2 level). Return only the assembly code and nothing else. Python code: "
    return "Convert the following Python code to x86-64 assembly (GAS, AT&T syntax), making aggressive optimizations, including algorithmic (Big O) improvements where possible. Return only the assembly code and nothing else. Python code: "

def compile_code(code, instruction, model="o4-mini", thinking_level="high"):
    OpenAI_key = os.getenv("OPENAI_API_KEY")

    if not OpenAI_key:
        print("Error finding API Key. Set the OPENAI_API_KEY environment variable.")
        sys.exit(1)

    client = OpenAI(api_key=OpenAI_key)

    prompt = instruction + code

    try:
        response = client.responses.create(
            model=model,
            reasoning={"effort": thinking_level},
            input=[
            {
            "role": "user", 
            "content": prompt
            }
         ],
        )
        assembly_code = response.output_text
        print(assembly_code)
        return assembly_code
    except Exception as err:
        print(f"Error during API call. Please try again in a few minutes: {err}")
        sys.exit(1)


def save_code(assembly_code, file_name):
    try:
        with open(f'{file_name}.s', 'w') as f:
            f.write(assembly_code)

    except Exception as err:
        print(f"Error saving compiled code. Please try regenerating.: {err}")
        sys.exit(1)

def run_code(file_name):
    try:
        os.system(f'gcc -o {file_name} {file_name}.s')
        os.system(f'./{file_name}')

    except Exception as err:
        print(f"Error running compiled code. Please try regenerating. Also, ensure gcc is installed: {err}")
        sys.exit(1)
