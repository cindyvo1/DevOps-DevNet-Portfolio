from test_data import *

def json_search(key, input_object):
    """
    Search a key from JSON object, get nothing back if key is not found
    key : "keyword" to be searched, case sensitive
    input_object : JSON object to be parsed, test_data.py in this case
    inner_function() is actually doing the recursive search
    return a list of key:value pair
    """
    ret_val = []   # nu lokaal binnen json_search

    def inner_function(key, input_object):
        if isinstance(input_object, dict):  # Iterate dictionary
            for k, v in input_object.items():
                if k == key:
                    ret_val.append({k: v})
                if isinstance(v, dict):
                    inner_function(key, v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str, int)):
                            inner_function(key, item)
        else:  # input_object is een lijst
            for val in input_object:
                if not isinstance(val, (str, int)):
                    inner_function(key, val)

    inner_function(key, input_object)
    return ret_val

print(json_search(key1, data))
