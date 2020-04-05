def len_title(contents):
    len_dict = {}

    for key, value in contents.items():
        key_length = len(str(key))
        value_length = len(str(value))
        if key_length > value_length:
            len_dict[key] = key_length
        else:
            len_dict[key] = value_length

    return len_dict


def to_line(contents, margin=1):
    line = '+'
    for value in contents.values():
        line += ('-' * (margin + value + margin)) + '+'
    return line


def to_header(contents, margin=1):
    header = '|'
    for key, value in contents.items():
        header += (' ' * margin)
        header += key
        if len(key) < value:
            header += (' ' * (value - len(key)))

        header += (' ' * margin) + '|'
    return header
