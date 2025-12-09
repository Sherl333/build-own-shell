import os
import sys
import subprocess

def main():
    # TODO: Uncomment the code below to pass the first stage
    builtin_commands = ['echo', 'exit', 'type']
    while True:
        sys.stdout.write("$ ")
        command = input().strip()
        if not command:
            continue
        parts = command.split()
        cmd = parts[0]
        if cmd == 'exit':
            break
        elif cmd == 'echo':
            print(" ".join(parts[1:]))
            continue
        elif cmd == 'type':
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
def find_executable(cmd):

    for directory in os.getenv("PATH", "").split(os.pathsep):
        full_path = os.path.join(directory, cmd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return None


if __name__ == "__main__":
    main()
