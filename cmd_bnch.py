import sys
import time
import subprocess

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <command> [args...]")
        sys.exit(1)

    command = sys.argv[1:]

    try:
        start_time = time.perf_counter()
        result = subprocess.run(command)
        end_time = time.perf_counter()
    except FileNotFoundError:
        print(f"Error: Command '{command[0]}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    elapsed = end_time - start_time
    print(f"Time elapsed: {elapsed:.3f} seconds")

    if result.returncode != 0:
        print(f"Note: The command exited with return code {result.returncode}.")

if __name__ == "__main__":
    main()
