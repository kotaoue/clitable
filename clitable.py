def print_table(contents, margin=1):
    print(_to_table(contents, margin))


def _to_table(contents, margin=1):
    titles = _len_title(contents)
    line = _to_line(titles)
    header = _to_header(titles)
    body = _to_body(titles, contents)

    table = ''
    table += line + '\n'
    table += header + '\n'
    table += line + '\n'
    table += '\n'.join(body) + '\n'
    table += line + '\n'

    return table


def _len_title(content_list):
    len_dict = {}

    for detail_dict in content_list:
        for key, value in detail_dict.items():
            item_length = max(len(str(key)), len(str(value)))
            if item_length > len_dict.get(key, 0):
                len_dict[key] = item_length

    return len_dict


def _to_line(title_dict, margin=1):
    line = '+'
    for value in title_dict.values():
        line += ('-' * (margin + value + margin)) + '+'
    return line


def _to_header(title_dict, margin=1):
    header = '|'

    for key, value in title_dict.items():
        header += (' ' * margin)
        header += key
        if len(key) < value:
            header += (' ' * (value - len(key)))

        header += (' ' * margin) + '|'
    return header


def _to_body(title_dict, content_list, margin=1):
    body = []

    for detail_dict in content_list:
        body_row = '|'
        for key, value in detail_dict.items():
            body_row += (' ' * margin)
            body_row += str(value)

            title_len = title_dict.get(key, 0)
            if len(str(value)) < title_len:
                body_row += (' ' * (title_len - len(str(value))))

            body_row += (' ' * margin) + '|'
        body.append(body_row)
    return body
