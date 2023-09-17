def correct_input():
    while True:
        try:
            num = float(input('Введите число:'))
            break
        except ValueError as e:
            print(f'Вы ввели не число. Ошибка: {e}')
    return num

if __name__ == '__main__':
    print(correct_input())