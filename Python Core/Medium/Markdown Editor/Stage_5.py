#  https://hyperskill.org/projects/162/stages/843/implement

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


def list(list_type):
    ar = []

    while True:
        a = int(input('Number of rows: '))

        if a < 1:
            print('The number of rows should be greater than zero')
            continue
        else:
            break

    for i in range(a):
        text = input(f'Row #{i+1}: ')
        if list_type == 'ordered-list':
            ar.append(f'{i+1}. {text}')
        else:
            ar.append(f'* {text}')

    return '\n'.join(ar) + '\n'


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
        case 'ordered-list':
            return list('ordered-list')
        case 'unordered-list':
            return list('unordered-list')


def save_result(text):
    with open('output.md', 'w') as result:
        result.write(text)


def main():
    formatters = "plain bold italic header link inline-code new-line ordered-list unordered-list"
    spec_com = "!help !done"
    text = ''

    while True:
        command = input('Choose a formatter: ')

        if command == '!done':
            save_result(text)
            break
        elif command == '!help':
            print(f"Available formatters: {formatters}", f"Special commands: {spec_com}", sep="\n")
            continue
        elif command not in formatters:
            print('Unknown formatting type or command')
            continue

        text += formatter(command)
        print(text)


if __name__ == '__main__':
    main()
