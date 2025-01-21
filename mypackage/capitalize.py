def capitalize(text):
    if text is None:
        return None
    if text == '':
        return ''
    return f'{text[0].upper()}{text[1:]}'

