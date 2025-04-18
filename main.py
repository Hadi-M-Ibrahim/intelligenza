import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="intelligenza: a CLI compiler that takes adavantage of LLMs directly compiling python into machine code."
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
        "source_file",
        help="Path to the source file to compile"
    )
    return parser.parse_args()


