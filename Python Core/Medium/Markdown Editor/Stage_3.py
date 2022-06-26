#  https://hyperskill.org/projects/162/stages/841/implement

def plain():
    return input('Text: ')


def bold():
    txt = input('Text: ')
    return f'**{txt}**'


def italic():
    txt = input('Text: ')
    return f'*{txt}*'


def inline_code():
    txt = input('Text: ')
    return f'`{txt}`'


def new_line():
    return '\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def header():
    while True:
        level = int(input('Level: '))

        if level > 6:
            print('The level should be within the range of 1 to 6')
            continue
        else:
            break

    txt = input('Text: ')
    return f"{'#' * level} {txt}\n"


def formatter(command):
    match command:
        case 'plain':
            return plain()
        case 'bold':
            return bold()
        case 'italic':
            return italic()
        case 'inline-code':
            return inline_code()
        case 'link':
            return link()
        case 'header':
            return header()
        case 'new-line':
            return new_line()


def main():
    formatters = "plain bold italic header link inline-code new-line"
    spec_com = "!help !done"
    text = ''

    while True:
        command = input('Choose a formatter: ')

        if command == '!done':
            break
        elif command == '!help':
            print(f"Available formatters: {formatters}", f"Special commands: {spec_com}", sep="\n")
        elif command not in formatters:
            print('Unknown formatting type or command')

        text += formatter(command)
        print(text)


if __name__ == '__main__':
    main()
