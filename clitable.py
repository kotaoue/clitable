def print_table(contents, margin=1):
    print(to_table(contents, margin))


def to_table(contents, margin=1):
    titles = len_title(contents)
    line = to_line(titles)
    header = to_header(titles)
    body = to_body(titles, contents)

    table = ''
    table += line + '\n'
    table += header + '\n'
    table += line + '\n'
    table += body + '\n'
    table += line + '\n'

    return table


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


def to_body(titles, contents, margin=1):
    body = '|'
    for key, value in contents.items():
        body += (' ' * margin)
        body += value

        title_len = titles[key]
        if len(value) < title_len:
            body += (' ' * (title_len - len(value)))

        body += (' ' * margin) + '|'
    return body
