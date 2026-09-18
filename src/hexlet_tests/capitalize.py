def capitalize(text):
    if text == '':
        return ''

    first_char = text[0].upper()
    rest_string = text[1:]
    return f'{first_char}{rest_string}'

print(capitalize('Hello'))
