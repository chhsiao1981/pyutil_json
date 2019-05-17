pyutil_json
==========

python utils for json

Usage
==========

dumps:

    import pyutil_json as json

    a = ['a', 'b', 'c']
    err, a_str = json.dumps_e(a)

    b = {'c': 'd', 'a': 'b'}
    err, b_str = json.dumps_e(b, sort_keys=True)

    c = [{'a': 'b', 'c': 'd'}]
    err, c_str = json.json_dumps_e(c, indent=2, sort_keys=True)

    d = set([1, 2, 3])
    json.dumps(d)  # expected raising exception

loads:

    a_str = '["a","b","c"]'
    err, a = json.loads_e(a_str)
