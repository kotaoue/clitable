"""clitable
Print table from list in argument.pi
"""


def print_table(contents, margin=1):
    """Print of table.

    Print table from list in argument.

    Args:
        contents (list): Print target.
        margin (int): Margin of each table column.

    Returns:
        void: Execute print method.

    """
    print(_to_table(contents, margin))


def _to_table(contents, margin=1):
    """Convert to table.

    Convert to table from list in argument.

    Args:
        contents (list): Print target.
        margin (int): Margin of each table column.

    Returns:
        str: Table string.

    """
    titles = _len_title(contents)
    line = _to_line(titles, margin)
    header = _to_header(titles, margin)
    body = _to_body(titles, contents, margin)

    table = ''
    table += line + '\n'
    table += header + '\n'
    table += line + '\n'
    table += '\n'.join(body) + '\n'
    table += line + '\n'

    return table


def _len_title(content_list):
    """Length of titles.

    Look up each column string`s length.

    Args:
        contents (list): Print target.

    Returns:
        str: Table string.

    """
    len_dict = {}

    for detail_dict in content_list:
        for key, value in detail_dict.items():
            item_length = max(len(str(key)), len(str(value)))
            if item_length > len_dict.get(key, 0):
                len_dict[key] = item_length

    return len_dict


def _to_line(title_dict, margin=1):
    """Convert to line.

    Convert to ruled line from each title info.

    Args:
        title_dict (dict): Each title info.
        margin (int): Margin of each table column.

    Returns:
        str: Ruled line.

    """
    line = '+'
    for value in title_dict.values():
        line += ('-' * (margin + value + margin)) + '+'
    return line


def _to_header(title_dict, margin=1):
    """Convert to header.

    Convert to header from from each title info.

    Args:
        title_dict (dict): Each title info.
        margin (int): Margin of each table column.

    Returns:
        str: Table header.

    """
    header = '|'

    for key, value in title_dict.items():
        header += (' ' * margin)
        header += key
        if len(key) < value:
            header += (' ' * (value - len(key)))

        header += (' ' * margin) + '|'
    return header


def _to_body(title_dict, content_list, margin=1):
    """Convert to body.

    Convert to body from from each title info.

    Args:
        title_dict (dict): Each title info.
        margin (int): Margin of each table column.

    Returns:
        str: Table body.

    """
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
