def polish_notation():
    command = ''
    while command != 'exit':
        inputted_string = input('Введите операцию (exit для выхода) ')
        try:
            symbols = inputted_string.split(' ')
            assert symbols[0] == '+' or symbols[0] == '-' or symbols[0] == '*' or symbols[0] == '/', 'Недопустимая операция'
            if symbols[0] == '+':
                print(int(symbols[1]) + int(symbols[2]))
            elif symbols[0] == '-':
                print(int(symbols[1]) - int(symbols[2]))
            elif symbols[0] == '*':
                print(int(symbols[1]) * int(symbols[2]))
            elif symbols[0] == '/':
                print(int(symbols[1]) // int(symbols[2]))
        except AssertionError:
            print('Недопустимая операция')
        except ZeroDivisionError:
            print('На 0 делить нельзя')
        except ValueError:
            print('Не введены числа')
        except IndexError:
            print('Неверное количество аргументов')
    print('Работа завершена')
polish_notation()