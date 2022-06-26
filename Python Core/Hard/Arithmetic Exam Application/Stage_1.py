# write your code here
first_num, sep, second_num = map(str, input().split())

match sep:
    case '+':
        print(int(first_num) + int(second_num))
    case '-':
        print(int(first_num) - int(second_num))
    case '*':
        print(int(first_num) * int(second_num))
