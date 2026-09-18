from hexlet_tests.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает не верно!')

if capitalize('') != '':
    raise Exception('Функция работает не верно')

print('Все тесты пройдены!')

