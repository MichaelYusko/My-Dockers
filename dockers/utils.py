"""Utils file"""


def get_all_fields_by(key: str, lst: list):
    """ Return fields by key from an objects.
    :param key: Key for fields, which you want to return
    :param lst: An array with fields
    :return: An array with fields.
    """
    fields = []
    try:
        for obj in lst:
            for name in obj[key]:
                fields.append(name)
    except KeyError:
        raise KeyError
    return fields


def get_field_by(field: str, lst: list):
    """ Return fields by key from an objects.
       :param field: Key for fields, which you want to return
       :param lst: An array with fields
       :return: An array with fields.
       """
    fields = []
    try:
        for obj in lst:
            fields.append(obj[field])
    except KeyError:
        raise KeyError
    return fields
