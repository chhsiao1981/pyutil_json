# -*- coding: utf-8 -*-

import rapidjson as json


def json_dumps_ne(json_struct, default='', indent=None, sort_keys=False):
    """Dump struct to json-str.

    Args:
        json_struct (TYPE): the struct to dump.
        default (str, optional): default if unable to dump.
        indent (int, optional): indent in dump.
        sort_keys (bool, optional): whether to sort-keys.

    Returns:
        TYPE: Description
    """
    err, result = json_dumps_e(json_struct, default, indent, sort_keys)

    return result


def json_dumps_e(json_struct, default='', indent=None, sort_keys=False):
    """Dump struct to json-str.

    Args:
        json_struct (TYPE): the struct to dump.
        default (str, optional): default if unable to dump.
        indent (int, optional): indent in dump.
        sort_keys (bool, optional): whether to sort-keys.

    Returns:
        TYPE: Description
    """
    err = None
    result = ''
    try:
        result = json.dumps(json_struct, indent=indent, sort_keys=sort_keys)
    except Exception as e:
        err = e
        result = default

    return err, result


def json_loads_ne(json_str, default=None):
    """Load from the json-str.

    Args:
        json_str (str): json-str.
        default (None, optional): default if unable to load.

    Returns:
        result: json-struct.
    """
    err, result = json_loads_e(json_str, default)

    return result


def json_loads_e(json_str, default=None):
    """Load from the json-str.

    Args:
        json_str (str): json-str.
        default (None, optional): default if unable to load.

    Returns:
        err: err.
        result: json-struct.
    """
    if default is None:
        default = {}

    err = None
    result = default

    try:
        result = json.loads(json_str)
    except Exception as e:
        err = e
        result = default

    return err, result
