import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == 'exit':
            return False
        elif command.startswith('type'):
            builtin_commands = ['echo', 'exit', 'type']
            typed_input = command.split('type ')[1]
            if typed_input in builtin_commands:
                print(f"{typed_input} is a shell builtin")
            else:
                print(f"{typed_input}: not found")

        elif command.startswith('echo'):
            messsage = command.split('echo ')[1]
            print(messsage)
        else:
            print(f"{command}: command not found")
        # main()


if __name__ == "__main__":
    main()
