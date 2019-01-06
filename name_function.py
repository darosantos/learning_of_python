def get_formatted_name(first, last):
    """Gera um nome completo formatado de modo elegante."""
    full_name = first + ' ' + last
    return full_name.title()


def get_formatted_name2(first, last, middle=''):
    """Gera um nome completo formatado de modo elegante."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()