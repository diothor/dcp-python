# O(n) where n is number of chunks in flatten keys
def flatten_dict(nested: dict) -> dict:
    flat = {}
    for key, value in nested.items():
        if isinstance(value, dict):
            for nested_key, nested_value in flatten_dict(value).items():
                flat[f'{key}.{nested_key}'] = nested_value
        else:
            flat[key] = value
    else:
        return flat


nested_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8,
            "bax": 11
        }
    }
}

assert flatten_dict(nested_dict) == {
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
