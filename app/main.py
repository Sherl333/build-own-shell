import os
import sys
import subprocess

def find_executable(cmd):
    """Return the full path of cmd if found in PATH and executable."""
    for directory in os.getenv("PATH", "").split(os.pathsep):
        full_path = os.path.join(directory, cmd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return None


def main():
    builtin_commands = ['echo', 'exit', 'type']

    while True:
        sys.stdout.write("$ ")
        user_input = input().strip()

        if not user_input:
            continue

        parts = user_input.split()
        cmd = parts[0]

        # -------------------------
        # BUILTIN: exit
        # -------------------------
        if cmd == "exit":
            break

        # -------------------------
        # BUILTIN: echo
        # -------------------------
        elif cmd == "echo":
            print(" ".join(parts[1:]))
            continue

        # -------------------------
        # BUILTIN: type
        # -------------------------
        elif cmd == "type":
            if len(parts) < 2:
                print("type: missing argument")
                continue

            target = parts[1]

            # Check builtin
            if target in builtin_commands:
                print(f"{target} is a shell builtin")
                continue

            # Search PATH
            exe_path = find_executable(target)
            if exe_path:
                print(f"{target} is {exe_path}")
            else:
                print(f"{target}: not found")
            continue

        # -------------------------
        # EXTERNAL PROGRAM
        # -------------------------
        else:
            exe_path = find_executable(cmd)
            if exe_path is None:
                print(f"{cmd}: not found")
                continue

            # Run the external program with all arguments
            try:
                subprocess.run([exe_path] + parts[1:])
            except Exception as e:
                print(f"{cmd}: error executing program")

            continue


if __name__ == "__main__":
    main()

