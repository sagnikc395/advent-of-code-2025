# script to compile the differet targets

import os
import sys
import subprocess

# configuration
# setitng the desired C++ standard
CPP_STANDARD = "-std=c++20"
# utility source file
UTILS_SOURCE = "src/utils/file_utils.cpp"
# flag to tell clang++ where to find the headers
INCLUDE_FLAG = "-Iinclude"


def compile_and_run_day(day_number: int):
    """
    handle compilation and execution for a specific Advent of Code day problem
    """
    try:
        day_number = int(day_number)
    except ValueError:
        print(f"Error: '{day_number}' is not a valid integer day number")
        sys.exit(1)

    day_source = f"src/day{day_number}.cpp"
    day_input = f"data/day{day_number}-input.txt"
    executable_name = f"day{day_number}.out"

    # validate source and data files
    if not os.path.exists(day_source):
        print(f"Error: Source file '{day_source}' not found.")
        sys.exit(1)

    # input file is often a necessary dependency
    if not os.path.exists(day_input):
        print(
            f"Wokring : Input file '{day_input}' not found. Program may fail it if expects it."
        )

    # compilation
    print(f"\n -> Compiling Day {day_number}: {day_source} ...")

    # list of arguments for clang++
    compile_command = [
        "clang++",
        CPP_STANDARD,
        INCLUDE_FLAG,
        day_source,
        UTILS_SOURCE,
        "-o",
        executable_name,
    ]

    # execute the compilation command
    try:
        compile_result = subprocess.run(
            compile_command, check=True, capture_output=True, text=True
        )
        print("Compilation successful.")

        if compile_result.stdout:
            print(compile_result.stdout)
        if compile_result.stderr:
            print(compile_result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"\n--- Compilation Fialed for Day {day_number} ---")
        print(e.stderr)
        # clean up partial executbale if any
        if os.path.exists(executable_name):
            os.remove(executable_name)
        sys.exit(1)
    except FileNotFoundError:
        print("ERROR: 'clang+' command not found. Install clang first")
        sys.exit(1)

    # 3. Execution Command
    print(f"\n-> Executing: ./{executable_name} {day_input}...")

    # The executable expects the input file path as its first argument
    execute_command = [f"./{executable_name}"]

    try:
        # Execute the compiled program
        subprocess.run(
            execute_command,
            check=True,
            capture_output=False,  # We want the program's output to go directly to the console
        )
        print("\nExecution finished successfully.")

    except subprocess.CalledProcessError as e:
        print(f"\n--- Execution Failed for Day {day_number} ---")
        print(e.stderr)
        sys.exit(1)

    finally:
        # 4. Cleanup (Optional: uncomment to keep your root directory clean)
        print(f"Cleaning up executable: {executable_name}")
        os.remove(executable_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compile.py <day_number>")
        print("Example: python compile.py 1")
        sys.exit(1)

    day = sys.argv[1]
    compile_and_run_day(int(day))
