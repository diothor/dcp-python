# O(n) where n is number of keys
def flatten_dict(nested_dict: dict, key_prefix: str = '') -> dict:
    flat_dict = {}
    for key, value in nested_dict.items():
        nested_key = f'{key_prefix}.{key}' if key_prefix else key
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, nested_key))
        else:
            flat_dict[nested_key] = value
    else:
        return flat_dict


test_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8,
            "bax": 11
        }
    }
}

assert flatten_dict(test_dict) == {
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8,
    "foo.bar.bax": 11,
}

geek_dict = {
    'geeks': {
        'Geeks': {
            'for': 7
        }
    },
    'Geeks': {
        'for': {
            'geeks': 4,
            'for': 1
        }
    },
    'for': {
        'geeks': {
            'Geeks': 3
        }
    }
}

assert flatten_dict(geek_dict) == {
    'geeks.Geeks.for': 7,
    'Geeks.for.geeks': 4,
    'Geeks.for.for': 1,
    'for.geeks.Geeks': 3
}

