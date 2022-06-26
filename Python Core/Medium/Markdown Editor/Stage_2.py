#  https://hyperskill.org/projects/162/stages/840/implement

def main():
    formatters = "plain bold italic header link inline-code ordered-list unordered-list new-line"
    spec_com = "!help !done"

    while True:
        command = input('Choose a formatter: ')

        if command == '!done':
            break
        elif command == '!help':
            print(f"Available formatters: {formatters}", f"Special commands: {spec_com}", sep="\n")
        elif command not in formatters:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    main()
