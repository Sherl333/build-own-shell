import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == 'exit':
            return False
        if command.startswith('echo'):
            messsage = command.split('echo ')[1]
            print(messsage)
        else:
            print(f"{command}: command not found")
        # main()


if __name__ == "__main__":
    main()
