import argparse
import os
from engine import load_file, opt_instruction, compile_code, save_code, run_code, delete_code

def parse_args():
    parser = argparse.ArgumentParser(
        description="intelligenza: a CLI compiler that takes adavantage of LLMs compiling python into machine code (x86-64 ASM)."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-o0",
        action="store_true",
        help="Optimization level: 0 (no optimization)"
    )
    group.add_argument(
        "-o1",
        action="store_true",
        help="Optimization level: 1 (standard optimization like what you would expect from a compiler)"
    )
    group.add_argument(
        "-o2",
        action="store_true",
        help="Optimization level: 2 [default] (aggressive optimization such as asymptotic/algrothimic optimization)"
    )
    parser.add_argument(
        "-e",
        action="store_true",
        help="Run code after compiling"
    )
    parser.add_argument(
        "-m", "--model",
        choices=["o4-mini", "o4-low", "o4-medium", "o4-high", "GPT-4.1"],
        default="o4-mini",
        help="OpenAI model to use for compilation"
    )
    parser.add_argument(
        "file",
        help="Path to the python file to compile should end in .py"
    )
    
    parser.add_argument(
        "-d",
        action="store_true",
        help="Delete the generated .s file after execution (default is to keep it)"
    )
    
    return parser.parse_args()


def main():
    print("compiling python to x86-64 assembly...")
    args = parse_args()
    file = args.file
    
    code = load_file(file)

    instruction = opt_instruction(args)

    assembly_code = compile_code(code, instruction, args.model)

    file_name = os.path.splitext(os.path.basename(file))[0]
    save_code(assembly_code, file_name)

    print(f"Assembly code saved to {file_name}.s")

    if args.e:
        print("Compiling and running the generated assembly...")
        run_code(file_name)

        if args.d:
            delete_code(file_name)

if __name__ == "__main__":
    main()
